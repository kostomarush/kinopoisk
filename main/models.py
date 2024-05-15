from django.db import models
from django.urls import reverse
    
class Acters(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class KinoFilms(models.Model):
    name = models.CharField(max_length=100)
    actors = models.ManyToManyField(Acters, blank=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('index')
    
class City(models.Model):
    city = models.CharField(max_length=100)
    
    def __str__(self):
        return self.city
    
class InfoActers(models.Model):
    MALE = 'M'
    FAMALE = 'F'

    GENDERS =  [
        
        (MALE, 'Мужчина'),
        (FAMALE, 'Женщина'),
        
    ]
    
    gender = models.CharField(max_length=1, choices=GENDERS)
    birthday = models.DateField()
    acter = models.OneToOneField(
        Acters,
        on_delete=models.CASCADE,
        primary_key=True
    )
    city = models.ForeignKey(
        City, 
        on_delete=models.SET_NULL, 
        null=True)
    
    def __str__(self):
        return self.acter.name
    
    
    
    
    

