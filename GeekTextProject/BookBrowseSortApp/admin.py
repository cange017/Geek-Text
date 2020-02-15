"""
    Mod Log:
    1/25 Miguel registerd Book and Author models
"""
from django.contrib import admin
from .models import Book
from .models import Author


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author','genre', 'price']


@admin.register(Author)
class Authordmin(admin.ModelAdmin):
  pass
