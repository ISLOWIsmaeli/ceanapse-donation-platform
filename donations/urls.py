from django.urls import path

from . import views

app_name = "donations"
# app_name = "donations"

urlpatterns = [
    path("donation/<int:donation_id>/", views.donation_checkout, name="donation"),
    path('donation-success/<int:project_id>/', views.donation_success, name='donation-success'),
    path('donation-failed/<int:project_id>/', views.donation_failed, name='donation-failed'),
    path('checkout/<int:project_id>/', views.create_paystack_checkout_session, name='donation-checkout'),
    path('webhook/paystack/', views.paystack_webhook),
]