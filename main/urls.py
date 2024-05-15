from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('acters/', views.acters, name='acters'),
    path('delete/<int:pk>/', views.remove_film, name='remove_film'),
    path('update/<int:pk>/', views.NewsUpdateView.as_view(), name='update'),
    path('add_film/', views.new_film, name='add_film'),
    path('add_actor/', views.new_actor, name='add_actor'),
    path('info_acters/<int:pk>/', views.info_acter, name='info_acters'),
    path('add_info_acter/', views.add_info_acter, name='add_info_acter'),
    path('remove_info/<int:pk>/', views.remove_info, name='remove_info'),
]
