from django import forms
from django.contrib.auth.models import User

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label='Nome de usuário', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite seu usuário"
            }
        )
    )
    
    senha = forms.CharField(
        label='Senha',
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )

class CadastroForms(forms.Form):
    nome_login = forms.CharField(
        label='Nome de usuário', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite seu usuário"
            }
        )
    )

    email = forms.CharField(
        label='Email',
        required=True, 
        max_length=70,
         widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite seu email"
            }
        )
    )
    
    senha = forms.CharField(
        label='Senha',
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )

    senha_confirm = forms.CharField(
        label='Confirmar senha',
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder": "Digite sua senha novamente"
            }
        )
        
    )

    def clean_nome_login(self):
        nome = self.cleaned_data.get('nome_login')

        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError('Nome de login não pode ter espaços!')
            
            elif User.objects.filter(username = nome).exists():
                raise forms.ValidationError('Usuario já existe!')
                
            else:
                return nome

    def clean_senha_confirm(self):
        senha_confirm = self.cleaned_data.get('senha_confirm')
        senha = self.cleaned_data.get('senha')

        if senha and senha_confirm:
            if senha != senha_confirm:
                raise forms.ValidationError('Senhas diferentes!')
            else:
                return senha_confirm
        else:
            raise forms.ValidationError('Insira ambas as senhas!')