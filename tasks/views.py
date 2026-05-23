from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    
    if request.method == 'POST':
        title = request.POST.get('title')
        Task.objects.create(title=title)
    
        return redirect('task_list')

    tasks = Task.objects.all()
    context = {'tasks': tasks}
    
    return render(request, 'tasks/task_list.html', context)

def delete_task(request, task_id):
    
    task = Task.objects.get(id=task_id)
    task.delete()
    
    return redirect('task_list')

def toggle_complete(request, task_id):
    
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    
    return redirect('task_list')

def edit_task(request, task_id):
    
    task = Task.objects.get(id=task_id)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        task.title = title
        task.save()
        
        return redirect('task_list')
    
    context = {'task': task}
    
    return render(request, 'tasks/edit_task.html', context)

