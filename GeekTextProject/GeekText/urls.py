"""Mod Log
1/25 Miguel imported url
     defined url for home and books
     added entry for static files for the project
1/26 Omar created login url and registration
"""
from django.contrib import admin
from django.urls import path, include
from BookBrowseSortApp import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^home/', views.home, name = 'home'),
    url(r'^books/', views.books, name='books'),
    url(r'^details/', views.details, name='details'),
    url(r'^cart/', views.cart, name='cart'),
    url(r'^checkout/', views.checkout, name='checkout'),
    url(r'^wishlist/', views.wishlist, name='wishlist'),
    url(r'^myaccount/', views.myaccount, name='myaccount'),
    url(r'^aboutt/', views.about, name='about'),
    #path('books/<int:pk>/', views.details, name='details'),
    #path('books/<int:id>', views.details, name='details'),
    path('accounts/', include('allauth.urls')),

    
]

urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)