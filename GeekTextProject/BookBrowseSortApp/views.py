"""
Mode Log
1/25 Miguel defined Http request for home and books URLs
1/26 Omar defined login and register
"""

from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required

def home(request):
     return render(request, 'home.html')
 

def books(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books':books})


