from django.db import models
from authUser.models import CustomUser

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return self.name