from django.urls import path
from .views import add_task, show_tasks, edit_task, delete_task

urlpatterns = [
    path('add/', add_task, name='add_task'),
    path('show/', show_tasks, name='show_tasks'),
    path('edit/<int:task_id>/', edit_task, name='edit_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
]
