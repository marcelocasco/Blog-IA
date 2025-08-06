from django import forms 
from .models import Noticia,Perfil
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NoticiaForm(forms.ModelForm):
    class Meta():
        model=Noticia
        fields=['titulo', 'contenido', 'categoria']

class PerfilForm(forms.ModelForm):
    class Meta:
        model=Perfil
        fields=['avatar','bio']

class RegistroUsuarioForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=['username','email','password1','password2']
