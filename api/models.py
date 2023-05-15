# Create your models here.

from django.contrib.auth.models import User
from django.db import models

GENERO_CHOICES = [
    ('DRAMA', 'DRAMA'),
    ('COMEDIA', 'COMÉDIA'),
]


class Filme(models.Model):
    nome = models.CharField(max_length=20)
    genero = models.CharField(choices=GENERO_CHOICES)
    ano = models.PositiveIntegerField()
    duracao = models.PositiveIntegerField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    

    