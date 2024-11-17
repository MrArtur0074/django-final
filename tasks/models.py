from django.db import models
from authUser.models import CustomUser
from projects.models import Project

# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ("P", 'Pending'),
        ("C", 'Completed'),
        ("F", 'Failed'),
    ]

    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='tasks')
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks_project')
    title = models.CharField(max_length=30)
    description = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    priority = models.IntegerField()
    complete_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Label(models.Model):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=7)

    def __str__(self):
        return self.name

class Task_Label(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.CASCADE)

    def __str__(self):
        return self