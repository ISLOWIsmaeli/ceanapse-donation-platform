from django.urls import path

from . import views

app_name = "donations"

urlpatterns = [
    path("", views.ocean_community, name="ocean_community"),
    path("donate/", views.donation_form, name="donation_form"),
    path("success/", views.donation_success, name="donation_success"),
    path("failed/", views.donation_failed, name="donation_failed"),
]