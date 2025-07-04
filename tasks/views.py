from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title.strip():
            Task.objects.create(title=title)
            messages.success(request, "Task added!")
        else:
            messages.warning(request, "Task title cannot be empty.")
        return redirect('index')

    tasks = Task.objects.all().order_by('-id')
    completed = Task.objects.filter(completed=True).count()
    total = Task.objects.count()

    return render(request, 'tasks/index.html', {
        'tasks': tasks,
        'completed': completed,
        'total': total
    })

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('index')

def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('index')

def clear_all(request):  # ✅ Add this at the bottom
    Task.objects.all().delete()
    messages.success(request, "All tasks cleared!")
    return redirect('index')
