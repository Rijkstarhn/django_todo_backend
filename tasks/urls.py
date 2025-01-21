from django.urls import path
from .views import TaskListAPI, TaskDetailAPI

urlpatterns = [
    path('tasks/', TaskListAPI.as_view(), name='task_list_api'),
    path('tasks/<int:pk>/', TaskDetailAPI.as_view(), name='task_detail_api'),
]