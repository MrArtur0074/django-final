from django.urls import path
from .views import TaskView, TaskViewSet

urlpatterns = [
    path('tasks/', TaskView.as_view(), name='tasks'),
    path('tasks/<int:task_id>/', TaskViewSet.as_view(), name='task')
]