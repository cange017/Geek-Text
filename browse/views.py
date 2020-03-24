from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book, Author
from django.shortcuts import render, redirect, get_object_or_404
from users.forms import RegistrationForm, AddCreditForm, AddressForm, ShipAddressForm
from django.contrib.auth.forms import UserChangeForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from users.models import Address, ShippingAddress, Payment
from django.forms import formset_factory
from django.db import models
from django.contrib.auth import get_user_model
from django.views.generic.edit import DeleteView
from django.views.generic import TemplateView, ListView#generic templates for search results Book App
from .models import Book
from django.db.models import Q

def home(request):
     books = Book.objects.all().order_by('releaseDate')[:4]
     return render(request, 'home.html', {'books': books})

def books(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'book-grid.html', {'books': books})

class SearchResultsView(ListView):#ListView,
    model = Book
    template_name = 'search_results.html'
    #queryset = Book.objects.filter(author__name__icontains='Miguel') # new
    def get_queryset(self): # 

        query = self.request.GET.get('q')
        criteria = self.request.GET.get('criteria')
        object_list = Book.objects.filter(
             Q(author__name__icontains=query) | Q(title__icontains=query)#author is foreingKey field
        ).filter ( Q(publisher__icontains=criteria))
        return object_list

def details(request, id):
    book_detail = get_object_or_404(Book, id=id)
    related_books = []
    # if the book count of particular author is greater than one
    if (Book.objects.filter(Q(author__name__icontains=book_detail.author)).count() > 1):
        # show all books by that author except for the current book
        related_books = Book.objects.filter(Q(author__name__icontains=book_detail.author)).exclude(Q(title__icontains= book_detail.title))
    return render(request, 'book-details.html',{'related_books': related_books ,'book': book_detail} )

def wishlist(request):
    return render(request, 'wishlist.html')

def myaccount(request):
    user = request.user
    addresses =  Address.objects.filter(users = user)
    ships = ShippingAddress.objects.filter(users = user)
    cards = Payment.objects.filter(user = user)

    return render(request, 'my-account.html', { 'user': user,'addresses': addresses,'cards': cards, 'ships':ships }) 
    
    if Address.objects.count()>0:
        instance = Address.objects.get(pk=1)
        form = AddressForm(instance=instance)
    if ShippingAddress.objects.count()>0:
        instance2 = ShippingAddress.objects.get(pk=1)
        form2 = ShipAddressForm(instance = instance2)
    if Payment.objects.count()>0:
        instance3 = Payment.objects.get(pk=1)
        form3 = AddCreditForm(instance = instance3)

    return render(request, 'my-account.html', { 'form2':form2, 'form3':form3 }) 

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

def address(request):
    if request.method =='POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False) # this insures it is assigned to user
            profile.save()
            profile.users.set([request.user.pk]) # many to many user save
            return redirect('myaccount')
    else:
        form = AddressForm()

    return render(request, 'address.html', {'form': form}) 

def shipaddress(request):
    if request.method =='POST':
        form = ShipAddressForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False) # this insures it is assigned to user
            profile.save()
            profile.users.set([request.user.pk]) #many to many user save
            return redirect('myaccount')
    else:
        form = ShipAddressForm()

    return render(request, 'shipaddress.html', {'form': form}) 

def addcard(request):
    if request.method =='POST':
        form = AddCreditForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False) # this insures it is assigned to user
            profile.user = request.user
            profile.save()
            return redirect('myaccount')
    else:
        form = AddCreditForm()

    return render(request, 'addcard.html', {'form': form}) 

class CardDelete(DeleteView):
    model = Payment
    success_url = reverse_lazy('myaccount')
    template_name = 'delete_card.html'

class ShippingDelete(DeleteView):
    model = ShippingAddress
    success_url = reverse_lazy('myaccount')
    template_name = 'delete_shipping.html'

class HomeDelete(DeleteView):
    model = Address
    success_url = reverse_lazy('myaccount')
    template_name = 'delete_home.html'

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def about(request):
    return render(request, 'about.html')