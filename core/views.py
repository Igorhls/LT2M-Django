from django.shortcuts import render
from .models import Bolsistas

def home(request):
    bolsistas = Bolsistas.objects.all()
    return render(request, 'index.html' , {'bolsistas': bolsistas})
