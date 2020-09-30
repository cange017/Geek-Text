"""geekT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from browse import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from browse.views import SearchResultsView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^home/', views.home, name = 'home'),
    url(r'^books/', views.books, name='books'),
    path('<int:id>', views.details, name='details'),
    url(r'^cart/', views.cart, name='cart'),
    url(r'^checkout/', views.checkout, name='checkout'),
    url(r'^wishlist/', views.wishlist, name='wishlist'),
    url(r'^myaccount/', views.myaccount, name='myaccount'),
    url(r'^aboutt/', views.about, name='about'),
    url(r'^register/$', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', views.logoutView, name = 'logout'),
    url(r'^address/$', views.address, name = 'address'),
    url(r'^shipaddress/$', views.shipaddress, name = 'shipaddress'),
    url(r'^addcard/$', views.addcard, name = 'addcard'),
    url(r'^delete_card/(?P<pk>\d+)/$', views.CardDelete.as_view(), name='delete_card'),
    url(r'^delete_shipping/(?P<pk>\d+)/$', views.ShippingDelete.as_view(), name='delete_shipping'),
    url(r'^delete_home/(?P<pk>\d+)/$', views.HomeDelete.as_view(), name='delete_home'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
]

urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)