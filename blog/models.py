from django.conf import settings
from django.db import models
from django.utils import timezone


"""Definição do modelo de postagem do blog"""
class Post(models.Model):
    """
    Definição da propriedade autor
    {ForeignKey} - Link para outro modelo
    """
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    """
    Definição da propriedade titulo
    {Charfield} - Texto com um número limitado de caracteres
    """
    title = models.CharField(max_length=200)
    
    """
    Definição da propriedade texto
    {TextField} - Textos sem um limite fixo
    """
    text = models.TextField()
    
    """
    Definição da propriedade data de postagem
    {DateTimeField} - data e hora
    """
    created_date = models.DateTimeField(default=timezone.now)
    
    """
    Definição da propriedade data de publicação
    {DateTimeField} - data e hora
    """
    published_date = models.DateTimeField(blank=True, null=True)

    """Método de publicação"""
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title