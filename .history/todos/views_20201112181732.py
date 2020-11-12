# from django.shortcuts import render
from rest_framework import viewsets

# from .serializers import *
# from .serializers import *
from .serializers import TodoSerializer
from todos.models import Todo


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
