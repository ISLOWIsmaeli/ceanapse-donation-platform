from django.shortcuts import render


def ocean_community(request):
  return render(request, "donations/ocean_community.html")


def donation_form(request):
  return render(request, "donations/donation_form.html")


def donation_success(request):
  # Get payment reference and other data from query parameters (Paystack redirect)
  reference = request.GET.get("reference", "")
  amount = request.GET.get("amount", "")
  donor_name = request.GET.get("donor_name", "")
  
  context = {
    "reference": reference,
    "amount": amount,
    "donor_name": donor_name,
  }
  return render(request, "donations/donation_success.html", context)


def donation_failed(request):
  # Get error details from query parameters
  reference = request.GET.get("reference", "")
  error_message = request.GET.get("error", "Payment could not be processed")
  
  context = {
    "reference": reference,
    "error_message": error_message,
  }
  return render(request, "donations/donation_failed.html", context)