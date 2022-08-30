from django.shortcuts import render, redirect
from .models import Tarefa
from .forms import FormTarefa


# Create your views here.
#LISTA TAREFAS CADASTRADAS
def lista_tarefa(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'tarefas.html', {'tarefas': tarefas})

#CADASTRAR NOVA TAREFA
def nova_tarefa(request):
    form = FormTarefa(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_tarefa')
    return render(request, 'formTarefa.html', {'form': form})

#ALTERAR TAREFA
def alterar_tarefa(request, id):
    tarefa = Tarefa.objects.get(id=id)
    form = FormTarefa(request.POST or None, instance=tarefa)

    if form.is_valid():
        form.save()
        return redirect('lista_tarefa')
    return render(request, 'formTarefa.html', {'form': form})

#REMOVER TAREFA
def remover_tarefa(request, id):
    tarefa = Tarefa.objects.get(id=id)
    
    if request.method == 'POST':
        tarefa.delete()
        return redirect('lista_tarefa')
    return render(request, 'confirma_delete.html', {'tarefa': tarefa})

