from django.shortcuts import render, redirect
from django.db import connection

def home(request):
    return render(request, 'home.html')