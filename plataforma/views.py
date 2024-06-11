from django.shortcuts import redirect, render
from django.urls import reverse

def homepage(request):
    return render(request, 'inicio.html')
