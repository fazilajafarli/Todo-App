from django.shortcuts import render
from rest_framework import generics
from todos.models import Todo
from .serializers import TodoSerializer

class TodoListApiView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetailApiView(generics.RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer




