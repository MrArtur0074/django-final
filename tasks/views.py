from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task
from .serializers import TaskSerializer


# Create your views here.
class TaskView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, project_id):
        tasks = Task.objects.filter(project_id=project_id)
        serializer = TaskSerializer(tasks, many=True)
        return Response({'tasks': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, project_id):
        dataProject = request.data.copy()
        dataProject['user_id'] = request.user.id
        dataProject['project_id'] = project_id
        serializer = TaskSerializer(data=dataProject)
        if serializer.is_valid():
            serializer.save()
            return Response({'task': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class TaskViewSet(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, project_id, task_id):
        tasks = Task.objects.filter(id=task_id)
        serializer = TaskSerializer(tasks, many=True)

        if len(tasks) == 0:
            return Response({'message': 'Такого задания нету у текущего проекта'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'task': serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, project_id, task_id):
        try:
            task = Task.objects.get(id=task_id, project_id=project_id)
        except Task.DoesNotExist:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

        dataProject = request.data.copy()
        dataProject['user_id'] = request.user.id
        dataProject['project_id'] = project_id

        serializer = TaskSerializer(task, data=dataProject)

        if serializer.is_valid():
            serializer.save()
            return Response({'task': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, project_id, task_id):
        try:
            task = Task.objects.get(id=task_id, project_id=project_id)
        except Task.DoesNotExist:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

        task.delete()
        return Response({"message" : "Задание удалено"}, status=status.HTTP_204_NO_CONTENT)
