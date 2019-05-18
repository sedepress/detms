from django.shortcuts import render
from django.shortcuts import render

def index(request):
    return render(request, 'tms/index.html', {})

def welcome(request):
    return render(request, 'tms/welcome.html', {})