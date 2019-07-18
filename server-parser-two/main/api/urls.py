from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [

    # [POST] Регистрация нового пользователя 
    path('register/', views.UserCreateAPIView.as_view()),
    
    # [POST] Авторизация имеющегося пользователя в БД
    path('auth/', obtain_auth_token),
    
    # [GET, POST, PUT] Получение, изменение и добавление задач
    path('task/', views.task),
    
    # [DELETE] Удаление задачи по ID
    path('task/<int:pk>/', views.TaskDeleteAPIView.as_view()),
]
