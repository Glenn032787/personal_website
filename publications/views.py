from django.shortcuts import render, redirect
from django.core.cache import cache
from django.contrib.auth.decorators import user_passes_test
from .models import Publication

# Create your views here.
def index(request):
    publications = Publication.objects.all()
    context = {'publications': publications}
    return render(request, "publications/index.html", context)
