from rest_framework import serializers
from django.contrib.auth import get_user_model
from . import models


class UserCreateSerializer(serializers.ModelSerializer):
    """Сериализация данных для регистрации данных."""
    class Meta:
        model = get_user_model()                          # Стандартная модель пользователя Django
        fields = ['username', 'password']                 # Показывать поля ЛОГИН и ПАРОЛЬ
        extra_kwargs = {'password': {'write_only': True}} # Пропуск проверки пароля со стандартами Django (доку не читал...)

    def create(self, validated_data):                     
        User = get_user_model()                           # Взять пользовательскую модель
        username = validated_data['username']             # Проверка и запись ЛОГИНА
        password = validated_data['password']             # Проверка и запись ПАРОЛЯ

        user_obj = User(username=username)                # Создание модели с ЛОГИНОМ
        user_obj.set_password(password)                   # Изменить пароль (пароль будет в зашифрованном варианте)
        user_obj.save()                                   # Сохранить модель 

        return validated_data                           


class TaskSerializer(serializers.ModelSerializer):
    """Сериализация данных для задач."""
    class Meta:
        model = models.Task     # Модель задач
        fields = '__all__'      # Показывать все поля модели
