from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
# Create your views here.


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_create.html', {'form': form})


def tasks_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks_list.html', {'tasks': tasks})
