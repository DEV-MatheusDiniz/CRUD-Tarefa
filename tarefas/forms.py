from django import forms
from .models import Tarefa


class FormTarefa(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = [
            'titulo',
            'descricao',
            'contato_id',
            'ativo'
        ]
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': "form-control"
            }),
            'descricao': forms.Textarea(attrs={
                'class': "form-control"
            }),
            'contato_id': forms.Select(attrs={
                'class': "form-control"
            }),
            'ativo': forms.CheckboxInput(attrs={
                'class': "form-check-input"
            })
        }
