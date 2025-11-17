from django.urls import path

from . import views

app_name = "projects"

urlpatterns = [
    path("ceanapse/", views.ceanapse_home, name="ceanapse-home"),
]