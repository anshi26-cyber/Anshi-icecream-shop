import os
from django.shortcuts import render
from .models import IceCream
from django.db.models import Q

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

# Services Subpages
def icecream(request):
    icecreams = IceCream.objects.all()
    return render(request, "icecream.html", {'icecreams': icecreams})

def Cone_and_Bar(request):
    icecreams = IceCream.objects.filter(name__icontains="Cone and Bar")
    return render(request, "Cone_and_Bar.html", {'icecreams': icecreams})

def Family_Pack_and_Cake(request):
    icecreams = IceCream.objects.filter(name__icontains="Family Pack and Cake")
    return render(request, "Family_Pack_and_Cake.html", {'icecreams': icecreams})

# Search Functionality
def search_view(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        results = IceCream.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    context = {
        'query': query,
        'results': results
    }
    return render(request, 'search_results.html', context)
