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
    url(r'^books/', views.books, name='books'),

    path('accounts/', include('allauth.urls')),

    url(r'^home/', views.home, name = 'home'),
]+ static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
