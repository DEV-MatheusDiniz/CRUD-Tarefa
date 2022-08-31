from django.db import models
from contatos.models import Contato


# Create your models here.
#TABELA DE TAREFAS
class Tarefa(models.Model):
    contato_id = models.ForeignKey(Contato, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=60)
    descricao = models.CharField(max_length=150)
    ativo = models.BooleanField()
    data_alteracao = models.DateTimeField('data/hora', null=True, blank=True)
    data_cadastro = models.DateTimeField('data/hora')


    def __str__(self):
        return self.titulo
        