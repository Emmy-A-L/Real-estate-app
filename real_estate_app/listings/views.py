from django.shortcuts import render, redirect


# Create your views here.

def listings(request):
    return render(request, 'listings.html')

def land_list(request):
    return render(request, 'land_list.html')

def houses_list(request):
    return render(request, 'houses_list.html')