from django.shortcuts import render, redirect, get_object_or_404
from .models import TaskModel
from .forms import TaskForm
from django.db.models import Q

def home(request):
    query = request.GET.get('search')
    if query:
        tasks = TaskModel.objects.filter(
            Q(taskTitle__icontains=query) | Q(taskDescription__icontains=query)
        )
    else:
        tasks = TaskModel.objects.all()
    return render(request, 'task/home.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            form.save_m2m()  # Save the many-to-many relationships
            return redirect('show_tasks')
    else:
        form = TaskForm()
    return render(request, 'task/add_task.html', {'form': form})

def show_tasks(request):
    tasks = TaskModel.objects.all()
    return render(request, 'task/show_tasks.html', {'tasks': tasks})

def edit_task(request, task_id):
    task = get_object_or_404(TaskModel, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            form.save_m2m()  # Save the many-to-many relationships
            return redirect('show_tasks')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task/edit_task.html', {'form': form})

def delete_task(request, task_id):
    task = get_object_or_404(TaskModel, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('show_tasks')
    return render(request, 'task/delete_task.html', {'task': task})
