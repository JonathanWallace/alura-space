from django import forms
from apps.galeria.models import Fotografia

class FotoForms(forms.ModelForm):
    class Meta:
        model = Fotografia
        exclude = ['publicado','usuario']

        

        labels = {
            'descricao':'Descrição',
            'foto': 'Imagem'
        }

        widgets = {
            'nome': forms.TextInput(attrs={"class":"form-control"}),
            'legenda': forms.TextInput(attrs={'class':"form-control"}),
            'categoria': forms.Select(attrs={'class':"form-control"}),
            'descricao': forms.Textarea(attrs={'class':"form-control"}),
            'foto': forms.FileInput(attrs={'class':"form-control"}),
            'usuario': forms.Select(attrs={'class':"form-control"}),

        }
