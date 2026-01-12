from django.shortcuts import render
from .models import Library

def home(request):
    libraries = Library.objects.all()
    return render(request, "relationship_app/home.html", {"libraries": libraries})

