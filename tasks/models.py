from django.db import models
from django.utils import timezone

PRIORITY_CHOICES = [
    ('High', 'High'),
    ('Medium', 'Medium'),
    ('Low', 'Low')
]

REPEAT_CHOICES = [
    ('None', 'None'),
    ('Daily', 'Daily'),
    ('Weekly', 'Weekly'),
    ('Monthly', 'Monthly')
]

class Task(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    repeat = models.CharField(max_length=10, choices=REPEAT_CHOICES, default='None')

    def __str__(self):
        return self.title

class TaskHistory(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    status_changed_at = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField()

    def __str__(self):
        return f"{self.task.title} - {'Done' if self.completed else 'Undone'}"
