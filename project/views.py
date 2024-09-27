from django.shortcuts import render, get_object_or_404
from .models import Project


# Create your views here.
def index(request):
    projects = Project.objects.all()

    context = {
        'projects': projects
    }
    return render(request, "project/index.html", context)

def individual_project(request, project_id):
    project_data = get_object_or_404(Project, id=project_id)
    return render(request, "project/individual_project.html", {"project_data": project_data})