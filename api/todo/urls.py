
from django.urls import path
from .views import ListCreateTaskView, TaskDetailView


urlpatterns = [
    path('tasks/', ListCreateTaskView.as_view(), name="tasks-list-create"),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name="tasks-detail")
]
