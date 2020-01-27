"""
Mode Log
1/25 Miguel defined Http request for home and books URLs
1/26 Omar defined login 
"""

from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

def home(request):
     return render(request, 'home.html')
 

def books(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books':books})

def login(request):
     return render(request, 'login.html')

