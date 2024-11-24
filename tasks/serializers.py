from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task

        fields = '__all__'

    def create(self, validated_data):

        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status', instance.status)
        instance.priority = validated_data.get('priority', instance.priority)
        instance.complete_date = validated_data.get('complete_date', instance.complete_date)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
        return instance