from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_task, name='add_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('toggle/<int:task_id>/', views.toggle_complete, name='toggle_complete'),
    path('clear/', views.clear_all, name='clear_all'),
    path('analytics/', views.analytics, name='analytics'),
]
