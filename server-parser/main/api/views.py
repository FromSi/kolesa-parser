from rest_framework import generics
from django.contrib.auth import get_user_model
from . import serializers, models
from .utils.create_notification import create
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


class UserCreateAPIView(generics.CreateAPIView):
    """Класс позволяет регистрировать пользователей."""
    serializer_class = serializers.UserCreateSerializer
    queryset = get_user_model().objects.all()


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def create_notification(request):
    """Метод позволяет записывать предпочтения пользователей.
    
    ЗАГОЛОВКИ-HTTP:
    Type-Update -- метод обновления (1-обновить данные, 2-обновить статус)

    Входные значения по DATA:
    status - статус активности для расылки
    mark -- ID марки машины
    type -- ID типа машины
    city -- ID города
    """
    if int(request.headers.get('Type-Update')) == 1: # error
        
        if request.data.get('mark'):
            mark = models.Mark.objects.get(id=request.data.get('mark'))
            mark = mark.value
        else:
            mark = ''
        
        if request.data.get('type'):
            t = models.Type.objects.get(id=request.data.get('type'))
            t = t.value
        else:
            t = ''
        
        if request.data.get('city'):
            city = models.City.objects.get(id=request.data.get('city'))
            city = city.value
        else:
            city = ''

        profile = models.Profile.objects.get(id=request.user.id)
        create(request.data, profile, mark, t, city)

        return Response(status=status.HTTP_200_OK)
    elif int(request.headers.get('Type-Update')) == 2: # error
        print(request.user.id)
        profile = models.Profile.objects.get(user__id=request.user.id)
        profile.active = request.data.get('status')
        profile.save()
        
        return Response(status=status.HTTP_200_OK)
    else:
        print(request.headers)
        return Response(status=status.HTTP_409_CONFLICT)