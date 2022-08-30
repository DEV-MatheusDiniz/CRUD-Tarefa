from django.db import models


# Create your models here.
#TABELA DE TAREFAS
class Tarefa(models.Model):
    titulo = models.CharField(max_length=60)
    descricao = models.CharField(max_length=150)
    ativo = models.BooleanField()

    def __str__(self):
        return self.titulo




