from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from .models import Task, TaskHistory
from django.db.models import Q

def index(request):
    tasks = Task.objects.all().order_by('-created_at')
    today = timezone.now().date()

    # Filtering and search
    query = request.GET.get('q', '')
    filter_status = request.GET.get('status', '')
    if query:
        tasks = tasks.filter(Q(title__icontains=query) | Q(category__icontains=query))
    if filter_status == 'completed':
        tasks = tasks.filter(completed=True)
    elif filter_status == 'pending':
        tasks = tasks.filter(completed=False)

    stats = {
        'total': Task.objects.count(),
        'completed': Task.objects.filter(completed=True).count(),
        'pending': Task.objects.filter(completed=False).count(),
        'today': Task.objects.filter(due_date=today).count(),
        'overdue': Task.objects.filter(due_date__lt=today, completed=False).count()
    }

    return render(request, 'tasks/index.html', {
        'tasks': tasks,
        'query': query,
        'filter_status': filter_status,
        'stats': stats,
        'today': today
    })

def add_task(request):
    if request.method == "POST":
        title    = request.POST.get("title", "").strip()
        category = request.POST.get("category", "").strip()
        due_date = request.POST.get("due_date") or None
        priority = request.POST.get("priority", "Medium")
        repeat   = request.POST.get("repeat", "None")

        if title:
            Task.objects.create(
                title=title,
                category=category,
                due_date=due_date,
                priority=priority,
                repeat=repeat,
            )
            messages.success(request, "Task added!")
        else:
            messages.warning(request, "Title cannot be empty.")
    return redirect("index")

def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    TaskHistory.objects.create(task=task, completed=task.completed)
    return redirect('index')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    messages.success(request, "Task deleted.")
    return redirect("index")

def clear_all(request):
    Task.objects.all().delete()
    messages.success(request, "All tasks cleared.")
    return redirect("index")

def analytics(request):
    all_tasks = Task.objects.all()
    completed_tasks = all_tasks.filter(completed=True)
    overdue_tasks = all_tasks.filter(due_date__lt=timezone.now().date(), completed=False)
    priority_count = all_tasks.values('priority').order_by().annotate(count=models.Count('priority'))

    return render(request, 'tasks/analytics.html', {
        'completed': completed_tasks.count(),
        'overdue': overdue_tasks.count(),
        'priority_count': priority_count,
    })
def toggle_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()

    # Optional: Record the change in history if using TaskHistory
    TaskHistory.objects.create(task=task, completed=task.completed)

    return redirect('index')
