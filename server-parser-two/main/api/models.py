from django.db import models
from django.contrib.auth import get_user_model

class Task(models.Model):
    """Задачи.

    Описание полей:
    url -- ссылка на парсинг конкретного объявления
    active -- статус дает понять, нужны ли объявления 
    user -- ссылка на пользователя
    email -- почта для уведомлений
    date -- дата последнего изменения статуса
    """
    url = models.CharField(max_length=255,
                           blank=True, 
                           null=True,
                           verbose_name='Ссылка')
    active = models.BooleanField(default=False,
                                 blank=True, 
                                 null=True,
                                 verbose_name='Статус')
    email = models.CharField(max_length=254,
                               blank=True, 
                               null=True,
                               verbose_name='Эл.почта')
    user = models.ForeignKey(get_user_model(), 
                             on_delete=models.CASCADE,
                             verbose_name='Пользователь')
    date = models.DateTimeField(auto_now=True,
                                verbose_name='Дата')
    
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        
    def __str__(self):
        return f'{self.email}'


class Ad(models.Model):
    """Объявления.

    Описание полей:
    uid -- ID объявления
    task -- ссылка на задачу
    """
    uid = models.PositiveIntegerField(blank=True, 
                                      null=True,
                                      verbose_name='UID')
    task = models.ForeignKey(Task, 
                             on_delete=models.CASCADE,
                             verbose_name='Задача')
    
    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        
    def __str__(self):
        return f'{self.uid}'