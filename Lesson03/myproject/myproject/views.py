#from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')
#    return HttpResponse("Home page")
    

def about(request):
    return render(request, 'about.html')
#    return HttpResponse("My about page")