from django.shortcuts import render
from rest_framework import viewsets, mixins
from .models import Task
from .serializer import TaskSerializer

class TaskViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
    ):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer