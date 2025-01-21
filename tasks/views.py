from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView

# Create your views here.
class TaskListAPI(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TaskDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer