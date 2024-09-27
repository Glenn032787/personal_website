from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="project"),
    path("id/<int:project_id>", views.individual_project, name="individual_project"),
]