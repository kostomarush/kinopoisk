from django.shortcuts import render, redirect
from .models import Acters, KinoFilms
from django.views.generic import UpdateView
from .forms import NewForm


def index(request):
    
    films = KinoFilms.objects.all()
    
    return render(request, 'main/index.html', {'films': films})

def acters(request):
    return render(request, 'main/acters.html')

class NewsUpdateView(UpdateView):
    model = KinoFilms
    template_name = 'main/new_form.html'
    form_class = NewForm

def remove_task(request, pk):
    item = KinoFilms.objects.get(pk=pk)
    item.delete()
    return redirect('index')

# def new_form(request):
#     error = ''
#     if request.method == 'POST':
#         form = NewForm(request.POST)
#         if form.is_valid():
#             f = form.save(commit=False)
#             f.save(using='tables')
#             return redirect('tables')
#     else:
#         error = 'Форма неверна!'

#     form = NewForm()
#     data = {
#         'form': form,
#         'error': error,
#     }
#     return render(request, 'user/new_form.html', data)