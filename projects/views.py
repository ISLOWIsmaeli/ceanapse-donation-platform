from django.shortcuts import render
from .models import Project
from django.shortcuts import get_object_or_404

def ceanapse_home(request):
  projects = Project.objects.all()
  context = {
    "projects": projects,
  }
  return render(request, "projects/ceanapse_home.html", context)

# list of projects
def project_list(request):
    projects = Project.objects.all()
    return render(request, "projects/project_list.html", {"projects": projects})