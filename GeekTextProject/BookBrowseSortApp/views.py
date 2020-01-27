"""
Mode Log
1/25 Miguel defined Http request for home and books URLs
1/26 Omar defined login and register
"""

from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .forms import RegistrationForm

def home(request):
     return render(request, 'home.html')
 

def books(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books':books})

def login(request):
     return render(request, 'login.html')

def register(request):
     if request.method == 'POST':
          form = RegistrationForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('/login')
     else:
          form= RegistrationForm()

          args = {'form': form}
          return render(request, 'register.html', args)

