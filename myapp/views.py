from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse("<h1>Welcome to the Home Page!</h1>")

def about(request):
    return HttpResponse("<h1>About Page</h1><p>This is the about page of the website.</p>")