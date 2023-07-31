from django.db import models

# Create your models here.
class AtendimentosPendentes(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField(max_length=150)
    message = models.TextField() 
    data = models.DateTimeField(auto_now_add=True)
