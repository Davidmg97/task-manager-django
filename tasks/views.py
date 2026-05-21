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

