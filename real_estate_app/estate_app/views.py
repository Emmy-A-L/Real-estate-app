from django.http import request
from django.shortcuts import render

# insert your views here

def home_page(request):
    return render(request, 'index.html')