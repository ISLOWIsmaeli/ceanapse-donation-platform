from django import forms
from .models import Donation

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['donor_full_name', 'donor_email', 'amount']
        widgets = {
            'donor_full_name': forms.TextInput(attrs={
                'placeholder': 'Enter your full name',
                'required': True
            }),
            'donor_email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email address',
                'required': True
            }),
            'amount': forms.NumberInput(attrs={
                'placeholder': 'Enter donation amount (NGN)',
                'min': '100',
                'step': '0.01',
                'required': True
            }),
        }
        labels = {
            'donor_full_name': 'Full Name',
            'donor_email': 'Email Address',
            'amount': 'Donation Amount (₦)',
        }