from django.db import models
import uuid 
from projects.models import Project
from django.contrib.auth.models import User



class DonationHistory(models.Model):
    email = models.EmailField(max_length=254, default='noemail@example.com')
    first_name = models.CharField(max_length=150, default='Anonymous', null=True, blank=True)
    last_name = models.CharField(max_length=150, default='User', null=True, blank=True)
    donation_id = models.CharField(max_length=225, default=uuid.uuid4())
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    donation_status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.donation_id

class PaystackDonation(models.Model):
    donation_history=models.ForeignKey(DonationHistory, null=True, blank=True, on_delete=models.SET_NULL)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, default='noemail@example.com')
    first_name = models.CharField(max_length=150, default='Anonymous', null=True, blank=True)
    last_name = models.CharField(max_length=150, default='User', null=True, blank=True)
    initialize_response=models.JSONField(null=True,blank=True,default=dict)
    call_back_response=models.JSONField(null=True,blank=True,default=dict)
    donation_id = models.CharField(max_length=225, default=uuid.uuid4())
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_success = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at=models.DateTimeField(null=True,blank=True, default=None)
