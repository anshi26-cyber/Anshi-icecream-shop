import os
from django.shortcuts import render
from .models import IceCream

# Home Page
def index(request):
    return render(request, "index.html")

# About Page
def about(request):
    return render(request, "about.html")

# Services Page
def services(request):
    return render(request, "services.html")

# Contact Page
def contact(request):
    return render(request, "contact.html")

def search(request):
    return render(request, 'search.html')


# Services Subpages
def icecream(request):
    return render(request, "icecream.html")

def cone_and_bar(request):
    return render(request, 'services/cone_and_bar.html')

def family_pack_and_cake(request):
    return render(request, "services/family_pack_and_cake.html")

