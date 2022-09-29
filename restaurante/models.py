from unittest.util import _MAX_LENGTH
from django.db import models

class prato(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.DecimalField(decimal_places=2, max_digits=18)
    imagem = models.ImageField(blank=True)

    def __str__(self):
        return self.nome


class auth_user(models.Model):
    pass
