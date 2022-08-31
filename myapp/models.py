from django.db import models
import datetime


# Create your models here.
#TABELA DE TAREFAS
class Tarefa(models.Model):
    titulo = models.CharField(max_length=60)
    descricao = models.CharField(max_length=150)
    ativo = models.BooleanField()
    data_alteracao = models.DateTimeField('data/hora', null=True, blank=True)
    data_cadastro = models.DateTimeField('data/hora', null=True, blank=True)


    def __str__(self):
        return self.titulo

