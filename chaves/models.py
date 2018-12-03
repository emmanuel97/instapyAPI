from django.db import models

class Chave(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    chave = models.CharField(max_length=100) # valor da chave Instapy
    dono = models.CharField(max_length=100) # dono da chave Instapy
    senha = models.CharField(max_length=100) # senha de recuperacao da chave Instapy
    ultimaOperacao = models.TextField()

    class Meta:
        ordering = ('created',)
