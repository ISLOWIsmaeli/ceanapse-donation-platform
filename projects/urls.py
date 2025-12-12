from django.urls import path

from . import views

app_name = "projects"

urlpatterns = [
    path("", views.ceanapse_home, name="ceanapse-home"),
]