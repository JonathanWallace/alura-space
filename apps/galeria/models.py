from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Fotografia(models.Model):

    CATEGORIAS = [('NEBULOSA', 'Nebulosa'), ('ESTRELA', 'Estrela'), ('GALAXIA', 'Galaxia'), ('PLANETA', 'Planeta')]

    nome = models.CharField(max_length=100, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=CATEGORIAS, default='')
    legenda = models.CharField(max_length=150, null=False, blank=False)    
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    publicado = models.BooleanField(default=True)
    usuario = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=False, related_name='user')

    def __str__(self):
        return f"Fotografia [nome={self.nome}]"