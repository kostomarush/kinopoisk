from django.shortcuts import render, redirect, get_object_or_404
from .models import Acters, KinoFilms, InfoActers
from django.views.generic import UpdateView
from .forms import NewForm, NewForm_films, NewActorForm, NewInfoActorForm

from django.core.exceptions import ObjectDoesNotExist




def index(request):
    
    films = KinoFilms.objects.all()
    
    return render(request, 'main/index.html', {'films': films})

def acters(request):

    all_actors = Acters.objects.all()

    error = ''
    if request.method == 'POST':
        form = NewActorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('acters')
        else:
            error = 'Форма не верна'

    form = NewActorForm()
    data = {

        'all_actors': all_actors,
        'form': form,
        'error': error,

    }

    return render(request, 'main/acters.html', data)

class NewsUpdateView(UpdateView):
    model = KinoFilms
    template_name = 'main/new_form.html'
    form_class = NewForm
    
def new_film(request):
    error = ''
    if request.method == 'POST':
        form = NewForm_films(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Форма не верна'
    form = NewForm_films()
    data = {
        'form': form,
        'error': error,

    }
    return render(request, 'main/new_film.html', data)

def new_actor(request):
    error = ''
    if request.method == 'POST':
        form = NewForm_films(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_actor')
        else:
            error = 'Форма не верна'
    form = NewForm_films()
    data = {
        'form': form,
        'error': error,

    }
    return render(request, 'main/new_acter.html', data)

def remove_film(request, pk):
    item = KinoFilms.objects.get(pk=pk)
    item.delete()
    return redirect('index')



def info_acter(request, pk):

    try:

        all_info = InfoActers.objects.get(pk=pk)

        data = {

            'all_info': all_info,

        }

        return render(request, 'main/info_acters.html', data)
    
    except ObjectDoesNotExist:

        all_actors = Acters.objects.all()

        error = ''
        if request.method == 'POST':
            form = NewActorForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('acters')
            else:
                error = 'Форма не верна'

        form = NewActorForm()

        alert_message = "Отсутствует описание данного актера"

        data = {

            'all_actors': all_actors,
            'form': form,
            'error': error,
            'alert_message': alert_message,

        }
        

        return render(request, 'main/acters.html', data)

def add_info_acter(request):

    error = ''
    if request.method == 'POST':
        form = NewInfoActorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('acters')
        else:
            error = 'Форма не верна'
            
    form = NewInfoActorForm()
    data = {
        'form': form,
        'error': error,

    }
    return render(request, 'main/add_info_acter.html', data)


def remove_info(request, pk):
    item = Acters.objects.get(pk=pk)
    item.delete()
    return redirect('acters')