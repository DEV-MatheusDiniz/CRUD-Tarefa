from django.db import models


# Create your models here.
#TABELA DE CONTATOS
class Contato(models.Model):
    nome = models.CharField(max_length=120)
    email = models.EmailField()
    data_alteracao = models.DateTimeField('data/hora', null=True, blank=True)
    data_cadastro = models.DateTimeField('data/hora')

    def __str__(self):
        return self.nome
        