from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="research"),
    path("update_database", views.update_database, name="update_database")
]