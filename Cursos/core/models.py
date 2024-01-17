from django.db import models

# Create your models here.
class Cursos(models.Model):
    titulo = models.CharField('titulo', max_length=100)
    vagas = models.IntegerField('vagas')