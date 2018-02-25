from django.http import HttpResponse
from django.shortcuts import render

def home(req):
    return render(req, 'home.html')
    #return HttpResponse('home')

def about(req):
    return render(req, 'about.html')
    #return HttpResponse('about')
