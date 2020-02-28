"""
Mode Log
1/25 Miguel defined Http request for home and books URLs
1/26 Omar defined login and register
"""

from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required

def home(request):
     books = Book.objects.all().order_by('releaseDate')[:4]
     return render(request, 'home.html', {'books': books})
 
def books(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'book-grid.html', {'books': books})

def details(request, id):
    book_detail = get_object_or_404(Book, id=id)
    return render(request, 'book-details.html', {'book': book_detail})
    
def wishlist(request):
    return render(request, 'wishlist.html')

def myaccount(request):
    return render(request, 'my-account.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def about(request):
    return render(request, 'about.html')
