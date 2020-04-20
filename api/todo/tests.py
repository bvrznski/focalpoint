
import json
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework.views import status
from .models import Task
from .serializers import TaskSerializer

# Create your tests here.
class TasksModelTest(APITestCase):
    """
    Tests the Task model class.
    """
    def setUp(self):
        self.a_task = Task.objects.create(
            title="Some task",
            description="Finish the task"
        )

    def test_task(self):
        self.assertEqual(self.a_task.title, "Some task")
        self.assertEqual(self.a_task.description, "Finish the task")
