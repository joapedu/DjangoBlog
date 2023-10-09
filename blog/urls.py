from django.urls import path
from . import views

"""
    Padrão de url '/'
    Atribuido a view post_list a url raiz
"""
urlpatterns = [
    path('', views.post_list, name='post_list')
]
