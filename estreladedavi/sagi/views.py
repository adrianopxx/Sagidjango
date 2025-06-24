from django.shortcuts import render

from django.urls import path

from django.http import HttpResponse

def home(request):
    return render(request, 'indice.html')  # renderiza o HTML

def sobre(request):
    return HttpResponse("Sobre nós.")

