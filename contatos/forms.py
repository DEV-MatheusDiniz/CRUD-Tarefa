from django import forms
from .models import Contato


class FormContato(forms.ModelForm):
    class Meta:
        model = Contato
        fields = [
            'nome',
            'email'
        ]
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': "form-control"
            }),
            'email': forms.EmailInput(attrs={
                'class': "form-control"
            })
        }
        