from django.db import models
from django.contrib.auth import get_user_model


class City(models.Model):
    """Города.

    Описание полей:
    name -- название города
    value -- текст для запроса по ссылке
    """
    name = models.CharField(max_length=255, 
                            blank=True, 
                            null=True,
                            verbose_name='Название')
    value = models.CharField(max_length=255, 
                             blank=True, 
                             null=True,
                             verbose_name='Значение')
    
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        
    def __str__(self):
        return f'{self.name} [{self.value}]'


class Mark(models.Model):
    """Марки машин.

    Описание полей:
    name -- название марки
    value -- текст для запроса по ссылке
    """
    name = models.CharField(max_length=255, 
                            blank=True, 
                            null=True,
                            verbose_name='Название')
    value = models.CharField(max_length=255, 
                             blank=True, 
                             null=True,
                             verbose_name='Значение')
    
    class Meta:
        verbose_name = 'Марка машины'
        verbose_name_plural = 'Марки машин'
        
    def __str__(self):
        return f'{self.name} [{self.value}]'


class Type(models.Model):
    """Тип машин.

    Описание полей:
    name -- название типа
    value -- текст для запроса по ссылке
    """
    name = models.CharField(max_length=255, 
                            blank=True, 
                            null=True,
                            verbose_name='Название')
    value = models.IntegerField(blank=True, 
                                null=True,
                                verbose_name='Значение')
    
    class Meta:
        verbose_name = 'Тип машины'
        verbose_name_plural = 'Типы машины'
        
    def __str__(self):
        return f'{self.name} [{self.value}]'


class Ad(models.Model):
    """Объявления.

    Описание полей:
    uid -- ID объявления
    title -- заголовок
    price -- цена
    description -- описание
    city -- город
    date -- дата создания
    views -- количество просмотров
    """
    uid = models.PositiveIntegerField(blank=True, 
                                        null=True,
                                        verbose_name='UID')
    title = models.CharField(max_length=255,
                             blank=True, 
                             null=True,
                             verbose_name='Заголовок')
    price = models.CharField(max_length=255,
                             blank=True, 
                             null=True,
                             verbose_name='Цена')
    description = models.CharField(max_length=255,
                                   blank=True, 
                                   null=True,
                                   verbose_name='Описание')
    city = models.CharField(max_length=255,
                            blank=True, 
                            null=True,
                            verbose_name='Город')
    date = models.CharField(max_length=255,
                            blank=True, 
                            null=True,
                            verbose_name='Дата')
    views = models.CharField(max_length=255,
                             blank=True, 
                             null=True,
                             verbose_name='Просмотры')
    
    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        
    def __str__(self):
        return f'{self.title} - {self.description}'


class Picture(models.Model):
    """Изображения.

    Описание полей:
    url -- ссылка на картинку
    ad -- ссылка на объявление
    """
    url = models.CharField(max_length=255,
                           blank=True, 
                           null=True,
                           verbose_name='Ссылка')
    ad = models.ForeignKey(Ad, 
                           on_delete=models.CASCADE,
                           verbose_name='Объявление')
    
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        
    def __str__(self):
        return f'{self.url}'


class Profile(models.Model):
    """Профиль.

    Описание полей:
    url -- ссылка на парсинг конкретного объявления
    active -- статус дает понять, нужны ли объявления для данного профиля
    user -- ссылка на пользователя
    """
    url = models.CharField(max_length=255,
                           blank=True, 
                           null=True,
                           verbose_name='Ссылка')
    active = models.BooleanField(default=False,
                                 blank=True, 
                                 null=True,
                                 verbose_name='Статус')
    user = models.ForeignKey(get_user_model(), 
                             on_delete=models.CASCADE,
                             verbose_name='Пользователь')
    
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        
    def __str__(self):
        return f'{self.user}'
