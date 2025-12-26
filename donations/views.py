import requests
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import uuid
from django.shortcuts import get_object_or_404
from .models import DonationHistory
from django.urls import reverse
from django.contrib import messages
from .paystack import checkout
from projects.models import Project
from .models import DonationHistory
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import hmac
import hashlib
import json
from django.contrib.auth.models import User
from decimal import Decimal, InvalidOperation
from django.conf import settings


def _donation_limits():
  min_amount = Decimal(str(getattr(settings, "DONATION_MIN_AMOUNT", 100)))
  max_amount = Decimal(str(getattr(settings, "DONATION_MAX_AMOUNT", 1000000)))
  return min_amount, max_amount

def donation_checkout(request, donation_id):
  project = Project.objects.get(id=donation_id)
  min_amount, max_amount = _donation_limits()
  context = {
    "project": project,
    "min_amount": min_amount,
    "max_amount": max_amount,
  }
  return render(request, "donations/donation_checkout_form.html", context)

@login_required # I propose donation success to be for everyone and we filter it at the templates level
def donation_success(request, project_id):

  project = Project.objects.get(id=project_id)
  
  # Get the most recent successful donation for this user and project
  donation = DonationHistory.objects.filter(
      user=request.user,
      project=project,
      donation_status=True
  ).order_by('-date').first()
  
  amount = donation.amount if donation else None
  donation_id = donation.donation_id if donation else None
  is_anonymous = donation.is_anonymous if donation else False
  donor_name = None if is_anonymous else (request.user.get_full_name() or request.user.username)

  return render(request, 'donations/donation_success.html', {
      'project': project,
      'amount': amount,
      'donation_id': donation_id,
      'donor_name': donor_name,
      'is_anonymous': is_anonymous,
  })

# no need to login 
def donation_failed(request, project_id):

  project = Project.objects.get(id=project_id)
    
  # Get the most recent failed donation for this user and project (optional)
  donation = DonationHistory.objects.filter(
      user=request.user,
      project=project,
      donation_status=False
  ).order_by('-date').first()
  
  amount = donation.amount if donation else None
  donation_id = donation.donation_id if donation else None
  
  return render(request, 'donations/donation_failed.html', {
      'project': project,
      'amount': amount,
      'donation_id': donation_id
  })


def create_paystack_checkout_session(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    amount = int(request.POST.get("amount", 0))
    is_anonymous = request.POST.get("is_anonymous") == "true"

    donation = DonationHistory.objects.create(
        project=project,
        user=request.user if request.user.is_authenticated else None,
        email=request.user.email if request.user.is_authenticated else request.POST.get("donor_email"),
        amount=amount,
        is_anonymous=is_anonymous,
        status="pending",
        reference=str(uuid.uuid4()),
    )

    # define required variables
    email = donation.email
    amount_kobo = int(donation.amount * 100)
    purchase_id = donation.reference
    callback_url = request.build_absolute_uri("/donations/callback/")

    first_name = request.POST.get("first_name", "")
    last_name = request.POST.get("last_name", "")
    phone = request.POST.get("phone", "")

    checkout_data = {
        "email": email,
        "amount": amount_kobo,
        "currency": "KES",
        "reference": purchase_id,
        "callback_url": callback_url,
        "metadata": {
            "purchase_id": purchase_id,
            "project_id": project.id,
            "is_anonymous": is_anonymous,
            "donor_email": email,
            "user_id": request.user.id if request.user.is_authenticated else None,
        }
    }

    if not is_anonymous:
        checkout_data["metadata"].update({
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone,
        })

    headers = {
        "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
        "Content-Type": "application/json",
    }

    response = requests.post(
        "https://api.paystack.co/transaction/initialize",
        json=checkout_data,
        headers=headers
    )

    res_data = response.json()

    if not res_data.get("status"):
        return JsonResponse({"error": "Payment initialization failed.", "details": res_data}, status=400)

    return redirect(res_data["data"]["authorization_url"])

@csrf_exempt
def paystack_webhook(request):
    secret = settings.PAYSTACK_SECRET_KEY
    request_body = request.body
    
    hash = hmac.new(secret.encode('utf-8'), request_body, hashlib.sha512).hexdigest()
    
    if hash == request.META.get('HTTP_X_PAYSTACK_SIGNATURE'):
        webhook_post_data = json.loads(request_body)
       
        if webhook_post_data["event"] == "charge.success":
            metadata = webhook_post_data["data"]["metadata"]
            data = webhook_post_data["data"]
            product_id = metadata["product_id"]
            user_id = metadata["user_id"]
            purchase_id = metadata["purchase_id"]

            amount_paid_kobo = data.get("amount")
            amount_paid = Decimal(amount_paid_kobo) / 100

            user = User.objects.get(id=user_id)

            is_anonymous = metadata.get("is_anonymous", False)
            if isinstance(is_anonymous, str):
                is_anonymous = is_anonymous.lower() == "true"

            DonationHistory.objects.create(
                donation_id = purchase_id,
                user = user,
                donation_status = True,
                project = Project.objects.get(id=product_id),
                amount = amount_paid,
                is_anonymous = is_anonymous
            )

            #send email to user on successful payment
            # send_payment_success_email(user.email, product_id)

    return HttpResponse(status=200)

   