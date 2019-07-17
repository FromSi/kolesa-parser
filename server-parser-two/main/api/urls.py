from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('register/', views.UserCreateAPIView.as_view()),
    path('auth/', obtain_auth_token),
    path('task/', views.task),
    path('task/<int:pk>/', views.TaskDeleteAPIView.as_view()),
]
