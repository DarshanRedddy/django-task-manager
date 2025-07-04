from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('toggle/<int:task_id>/', views.toggle_task, name='toggle_complete'),  # match the view name
    path('clear/', views.clear_all, name='clear_all'),  # ✅ This is what was missing
]
