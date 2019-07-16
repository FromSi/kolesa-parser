from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from . import serializers, models, handler_ads
from .utils.create_notification import create
from .utils import email
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail


class UserCreateAPIView(generics.CreateAPIView):
    """Класс позволяет регистрировать пользователей."""
    serializer_class = serializers.UserCreateSerializer
    queryset = get_user_model().objects.all()


@api_view(['GET', 'DELETE', 'POST'])
@permission_classes((IsAuthenticated,))
def email_profile(request):
    """Изменение или удаление почты.
    
    Аргументы для POST:
    email -- почта для будующих уведомлений
    """
    profile = models.Profile.objects.get(user_id=request.user.id)

    if request.method == 'DELETE':
        profile.email = None
        profile.save()

        return Response(status=status.HTTP_200_OK)
    elif request.method == 'GET':
        profile = models.Profile.objects.get(user_id=request.user.id)        
        return Response({'email': profile.email, 'active': profile.active}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        if request.data.get('email') != None:
            profile.email = request.data.get('email')
            profile.save()

            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((AllowAny,))
def get_filters_data(request):
    t = serializers.TypeSerializer(models.Type.objects.all(), many=True).data
    mark = serializers.MarkSerializer(models.Mark.objects.all(), many=True).data
    city = serializers.CitySerializer(models.City.objects.all(), many=True).data

    return Response({
        'type': t,
        'mark': mark,
        'city': city
    })


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_user_ads(request):
    """Получить все объявления пользователя."""
    answer = []
    ads = models.Profile.objects.get(user_id=request.user.id).ad.all()

    for ad in ads:
        list_picture = []
        pictures = models.Picture.objects.filter(ad_id=ad.id)
        
        for picture in pictures:
            list_picture.append(picture.url)
        
        ad = serializers.AdListSerializer(ad).data
        ad['pictures'] = list_picture
        answer.append(ad)

    return Response(answer)
    

@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def clear_all_ads(request):
    """Очистить список объявлений профиля."""
    profile = models.Profile.objects.get(user_id=request.user.id)
    profile.ad.clear()

    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def update_filter(request):
    """Метод позволяет записывать предпочтения пользователей.
    
    ЗАГОЛОВКИ-HTTP:
    Type-Update -- метод обновления (1-обновить данные, 2-обновить статус)

    Входные значения по DATA:
    status - статус активности для расылки
    mark -- ID марки машины
    type -- ID типа машины
    city -- ID города
    """
    try:
        if request.data.get('status') == None:
            if request.data.get('mark') != None:
                mark = models.Mark.objects.get(id=request.data.get('mark'))
                mark = mark.value
            else:
                mark = None

            if request.data.get('type') != None:
                t = models.Type.objects.get(id=request.data.get('type'))
                t = t.value
            else:
                t = None

            if request.data.get('city') != None:
                city = models.City.objects.get(id=request.data.get('city'))
                city = city.value
            else:
                city = None

            profile = models.Profile.objects.get(user_id=request.user.id)
            create(request.data, profile, mark, t, city)

            return Response(request_site(profile), status=status.HTTP_200_OK)
        elif request.data.get('status') != None:
            profile = models.Profile.objects.get(user_id=request.user.id)
            profile.active = request.data.get('status')
            profile.save()

            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_409_CONFLICT)
    except models.Profile.DoesNotExist:
        return Response(status=status.HTTP_409_CONFLICT)


def request_site(profile):
    ad_list = handler_ads.start(profile, 1)

    if profile.email != None:
        email.send(ad_list, profile.email)

    return ad_list
