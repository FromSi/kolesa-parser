from django.db import models
from django.contrib.auth.models import User


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


class Price(models.Model):
    """Цена.

    Описание полей:
    from_price -- цена от
    to_price -- цена до
    """
    from_price = models.PositiveIntegerField(blank=True, 
                                             null=True,
                                             verbose_name='Цена от')
    to_price = models.IntegerField(blank=True, 
                                   null=True,
                                   verbose_name='Цена до')
    
    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'
        
    def __str__(self):
        return f'{self.from_price}-{self.to_price}'


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
    user = models.ForeignKey(User, 
                             on_delete=models.CASCADE,
                             verbose_name='Пользователь')
    
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        
    def __str__(self):
        return f'{self.user}'
