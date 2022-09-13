from django.urls import path
from .views import TodoDetailApiView, TodoListApiView

urlpatterns = [
    path('', TodoListApiView.as_view()),
    path('<int:pk>/', TodoDetailApiView.as_view())
]
