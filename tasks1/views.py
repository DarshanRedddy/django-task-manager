from django.shortcuts import render, redirect
from .models import Task

def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
        return redirect('index')
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})
