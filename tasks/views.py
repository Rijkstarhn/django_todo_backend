from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView

from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class TaskListAPI(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['completed'] 
    
class TaskDetailAPI(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Task.objects.all()
    serializer_class = TaskSerializer