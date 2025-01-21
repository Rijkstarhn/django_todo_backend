from django.urls import path
from .views import TaskListAPI

urlpatterns = [
    path('tasks/', TaskListAPI.as_view(), name='task_list_api'),
]