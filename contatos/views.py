from django.shortcuts import render, redirect
from .models import Contato
from .forms import FormContato
import datetime

# Create your views here.
#LISTA DE CONTATOS CADASTRADOS
def lista_contatos(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos.html', {'contatos': contatos})

#CADASTRAR NOVO CONTATO
def novo_contato(request):
    form = FormContato(request.POST or None)

    if form.is_valid():
        new_form = form.save(commit=False)
        new_form.data_cadastro = datetime.datetime.now()
        new_form.save()
        return redirect('lista_contatos')
    return render(request, 'formContato.html', {'form': form})

#ALTERAR CONTATO
def alterar_contato(request, id):
    contato = Contato.objects.get(id=id)
    form = FormContato(request.POST or None, instance=contato)

    if form.is_valid():
        new_form = form.save(commit=False)
        new_form.data_alteracao = datetime.datetime.now()
        new_form.save()
        return redirect('lista_contatos')
    return render(request, 'formContato.html', {'form': form})
        

#REMOVER CONTATO
def remover_contato(request, id):
    contato = Contato.objects.get(id=id)

    if request.method == 'POST':
        contato.delete()
        return redirect('lista_contatos')
    return render(request, 'confirma_delete.html', {'contato': contato})