from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project

        fields = '__all__'

    def create(self, validated_data):

        return Project.objects.create(**validated_data)