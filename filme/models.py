from django.db import models
from django.utils import timezone

LISTA_CATEGORIAS = {
  ('ROCK', 'Rock'),
  ('POP', 'Pop'),
  ('MPB', 'MPB'),
  ('OUTROS', 'Outros'),
}


class Filme(models.Model):
  titulo = models.CharField(max_length=100)
  thumb = models.ImageField(upload_to='thumb_filmes')
  descricao = models.TextField(max_length=1000)
  categoria = models.CharField(max_length=10, choices=LISTA_CATEGORIAS)
  visualizacoes = models.IntegerField(default=0)
  data_criacao = models.DateTimeField(default=timezone.now())
  
  def __str__(self):
    return self.titulo