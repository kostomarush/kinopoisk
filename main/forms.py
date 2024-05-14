from django import forms
from .models import KinoFilms

class NewForm(forms.ModelForm):
    class Meta:
        model = KinoFilms
        fields = ['name', 'actors']

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Имя актера',
            }),
            'actors': forms.Select(attrs={
                'placeholder': 'Актеры',

            })
        }