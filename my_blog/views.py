from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    #return HttpResponse('home_page')
    return render(request, 'home_page.html')

def about(request):
    #return HttpResponse('about')
    return render(request, 'about.html')