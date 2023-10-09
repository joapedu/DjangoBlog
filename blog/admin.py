from django.contrib import admin
from .models import Post

"""Modelo visível na página de administração"""
admin.site.register(Post)