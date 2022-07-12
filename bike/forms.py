from django import forms
from django.forms import ModelForm
from .models import Bicicleta
from django.contrib.auth.forms import UserCreationForm


class BicicletaForm(ModelForm):
    class Meta:
        model = Bicicleta
        fields = ['idBicicleta', 'marca', 'imagen', 'descripcionBicicleta', 'precio', 'tipoBicicleta']
        
class CustomUserCreationForm(UserCreationForm):
    pass