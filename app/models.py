from django.db import models

# Create your models here.
class Filmes(models.Model):
    nome = models.CharField(max_length=150)
    gênero = models.CharField(max_length=100)
    ano = models.IntegerField()