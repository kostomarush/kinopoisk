from django import forms
from .models import KinoFilms, Acters, InfoActers

class NewForm(forms.ModelForm):
    class Meta:
        model = KinoFilms
        fields = ['actors']
    
        widgets = {
            'actors': forms.SelectMultiple()
            }
        
class NewForm_films(forms.ModelForm):
    class Meta:
        model = KinoFilms
        fields = ['name', 'actors']
    
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Имя фильма', 
            }),
            'actors': forms.SelectMultiple()
            }
        
class NewActorForm(forms.ModelForm):
    class Meta:
        model = Acters
        fields = ['name',]
    
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Полное имя актера', 
            })}

class NewInfoActorForm(forms.ModelForm):
    class Meta:
        model = InfoActers
        fields = ['acter', 'gender', 'birthday', 'city']

        MALE = 'M'
        FAMALE = 'F'

        GENDERS =  [
        
            (MALE, 'Мужчина'),
            (FAMALE, 'Женщина'),
        
            ]

        widgets = {
            'acter': forms.Select(attrs={
                'placeholder': 'Имя актера', 
            }),
            'gender': forms.Select(choices=GENDERS),

            'birthday': forms.DateInput(attrs={
                'placeholder': 'Дата Рождения: yyyy-mm-dd'}),

            'city': forms.Select()
            }