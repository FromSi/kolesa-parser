from django.shortcuts import render
from rest_framework import generics, permissions, status
from django.contrib.auth import get_user_model
from . import serializers, models
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import validators


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.UserCreateSerializer
    queryset = get_user_model().objects.all()

class TaskDeleteAPIView(generics.DestroyAPIView):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer
    permission_classes = (permissions.IsAuthenticated,)

@api_view(['GET', 'POST', 'PUT'])
@permission_classes((IsAuthenticated,))
def task(request):
    if request.method == 'GET':
        task = models.Task.objects.filter(user__id=request.user.id)
        
        return Response(serializers.TaskSerializer(task, many=True).data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        if request.data.get('url') != None \
                and validators.url(request.data.get('url')) \
                and request.data.get('email') \
                and validators.email(request.data.get('email')):
            task = models.Task(
                url=request.data.get('url'),
                email=request.data.get('email'),
                active=True,
                user=request.user
            )

            task.save()
            
            return Response(serializers.TaskSerializer(task).data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        task = models.Task.objects.get(id=request.data.get('id'))
        task.url = request.data.get("url") if request.data.get("url") != None and validators.url(request.data.get("url")) else task.url
        task.email = request.data.get("email") if request.data.get("email") != None and validators.email(request.data.get("email")) else task.email
        task.active = request.data.get("active") if request.data.get("active") != None else task.active
        task.save()

        return Response(serializers.TaskSerializer(task).data, status=status.HTTP_200_OK)