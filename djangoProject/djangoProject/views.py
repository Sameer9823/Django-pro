from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, world. You're at the djangoProject home page.")
    return render(request, 'website/index.html')

def about(request):
    # return HttpResponse("Hello, world. You're at the djangoProject about page.")
    return render(request, 'about/about.html')

def contact(request):
    return HttpResponse("Hello, world. You're at the djangoProject contact page.")


