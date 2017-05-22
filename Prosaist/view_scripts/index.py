from django.shortcuts import render

# Create your view_scripts here.
from django.http import HttpResponse


def view(request):
    return render(request, "base.html")
