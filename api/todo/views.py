from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import status

from .decorators import validate_request_data
from .models import Task
from .serializers import TaskSerializer, TokenSerializer, UserSerializer


class ListCreateTaskView(generics.ListCreateAPIView):
    """
    GET     /api/v1/tasks/     -> Retrieve list of tasks
    POST    /api/v1/tasks/     -> Create a new task
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @validate_request_data
    def post(self, request, *args, **kwargs):
        a_task = Task.objects.create(
            title=request.data["title"],
            description=request.data["description"]
        )
        return Response(
            data=TaskSerializer(a_task).data,
            status=status.HTTP_201_CREATED
        )


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET     /api/v1/tasks/[task_id]     -> Retrieve a task
    PUT     /api/v1/tasks/[task_id]     -> Update an existing task
    DELETE  /api/v1/tasks/[task_id]     -> Delete a task
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get(self, request, *args, **kwargs):
        try:
            a_task = self.queryset.get(pk=kwargs["pk"])
            return Response(TaskSerializer(a_task).data)
        except Task.DoesNotExist:
            return Response(
                data={
                    "message": "Task with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @validate_request_data
    def put(self, request, *args, **kwargs):
        try:
            a_task = self.queryset.get(pk=kwargs["pk"])
            serializer = TaskSerializer()
            updated_task = serializer.update(a_task, request.data)
            return Response(TaskSerializer(updated_task).data)
        except Task.DoesNotExist:
            return Response(
                data={
                    "message": "Task with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            a_task = self.queryset.get(pk=kwargs["pk"])
            a_task.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Task.DoesNotExist:
            return Response(
                data={
                    "message": "Task with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
