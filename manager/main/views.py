from django.shortcuts import render, redirect
from .models import Task
from .form import TaskForm

def index(request):
    tasks = Task.objects.order_by('-id')
    ctx = {'title': 'Home', 'tasks': tasks}
    return render(request, 'main/index.html', ctx )

def about(request):
    return render(request, 'main/about.html')

def create(request):
    err = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else: 
            err = "Form is't valid..."

    form = TaskForm()
    ctx = {
        'form': form,
        'error': err
    } 
    return render(request, 'main/create.html', ctx)