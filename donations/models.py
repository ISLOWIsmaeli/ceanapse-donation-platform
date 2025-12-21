from django.db import models
import uuid 
from projects.models import Project
from django.contrib.auth.models import User

class DonationHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    donation_id = models.CharField(max_length=225, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    donation_status = models.BooleanField(default=False)
    is_anonymous = models.BooleanField(default=False)
    email = models.EmailField(max_length=255, null=True, blank=True)  # new field
    status = models.CharField(max_length=50, default="pending")       # new field
    reference = models.CharField(max_length=255, null=True, blank=True) # new field
    date = models.DateTimeField(auto_now_add=True)
