from django.urls import path
from .views import lista_contatos, novo_contato, alterar_contato, remover_contato


urlpatterns = [
    path('contatos/', lista_contatos, name='lista_contatos'),
    path('novo-contato/', novo_contato, name='novo_contato'),
    path('alterar-contato/<int:id>/', alterar_contato, name='alterar_contato'),
    path('remover-contato/<int:id>/', remover_contato, name='remover_contato')
]