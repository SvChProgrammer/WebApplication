from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.order_by('title')
    return render(request, 'main/index.html', {'title': 'Главная страница моего сайта', 'tasks':tasks})


def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    if request.method == 'POST': #если данные переданы методом POST
        form = TaskForm(request.POST)
        if form.is_valid(): #если данные корректны
            form.save() #данные из формы сохраняються
            return redirect('home') #переадресовываем пользователя на страницу home
        else:
            error = 'Форма неккореткна'


    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)