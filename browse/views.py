from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book
from django.shortcuts import render, redirect, get_object_or_404
from users.forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy


def home(request):
     books = Book.objects.all().order_by('releaseDate')[:4]
     return render(request, 'home.html', {'books': books})
 
def books(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'book-grid.html', {'books': books})

def details(request, id):
    book_detail = get_object_or_404(Book, id=id)
    return render(request, 'book-details.html', {'book': book_detail})

# def books_by_author(self, author):
#     return Book.objects.filter(author=self.author).values_list(author,flat=True)
#   a.book_set.all()

def wishlist(request):
    return render(request, 'wishlist.html')

def myaccount(request):
   return render(request, 'my-account.html')
    
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')            
    else:
        form = RegistrationForm()
        
    return render(request, 'register.html', {'form': form})

def logoutView(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def about(request):
    return render(request, 'about.html')