from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Project
from .serializers import ProjectSerializer


# Create your views here.
class ProjectView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        projects = Project.objects.filter(user_id=request.user.id)

        serializer = ProjectSerializer(projects, many=True)

        return Response({'projects': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        dataProject = request.data.copy()
        dataProject['user_id'] = request.user.id

        serializer = ProjectSerializer(data=dataProject)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Project created successfully'}, status=status.HTTP_201_CREATED)

        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)