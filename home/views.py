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

def cone_and_bar(request):
    icecreams = IceCream.objects.filter(name__icontains="cone and bar")
    return render(request, 'services/cone_and_bar.html', {'icecreams': icecreams})

def family_pack_and_cake(request):
    icecreams = IceCream.objects.filter(name__icontains="family pack and cake")
    return render(request, "services/family_pack_and_cake.html", {'icecreams': icecreams})

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