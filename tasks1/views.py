from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Task

def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
        return redirect('index')
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})

def index(request):
    # ────── create ──────
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        if title:
            Task.objects.create(title=title)
            messages.success(request, "✅ Task added")
        else:
            messages.warning(request, "⚠️  Title cannot be empty")
        return redirect('index')

    # ────── read ──────
    tasks      = Task.objects.all().order_by('-id')
    completed  = tasks.filter(completed=True).count()
    pending    = tasks.filter(completed=False).count()

    context = {
        'tasks': tasks,
        'completed': completed,
        'pending': pending,
    }
    return render(request, 'tasks/index.html', context)


def toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect('index')


def delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    messages.info(request, "🗑️  Task deleted")
    return redirect('index')


def clear(request):
    Task.objects.all().delete()
    messages.success(request, "🧹 Cleared all tasks")
    return redirect('index')
