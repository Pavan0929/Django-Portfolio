from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("Hello world!")

def home(request):
    return render(request, 'members/home.html')

def profile(request):
    return render(request, 'members/profile.html')    

def about(request):
    return render(request, 'members/about.html')        