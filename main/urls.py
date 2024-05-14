from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('acters/', views.acters, name='acters'),
    path('delete/<int:pk>/', views.remove_task, name='remove_film'),
    path('update/<int:pk>', views.NewsUpdateView.as_view(), name='update'),
]
