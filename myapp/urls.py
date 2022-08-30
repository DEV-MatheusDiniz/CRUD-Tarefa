from django.urls import path
from .views import lista_tarefa, nova_tarefa, alterar_tarefa, remover_tarefa


urlpatterns = [
    path('', lista_tarefa, name='lista_tarefa'),
    path('nova-tarefa/', nova_tarefa, name='nova_tarefa'),
    path('alterar-tarefa/<int:id>/', alterar_tarefa, name='alterar_tarefa'),
    path('remover-tarefa/<int:id>/', remover_tarefa, name='remover_tarefa'),
]