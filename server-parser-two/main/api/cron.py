from . import models, handler_ads
from .utils import email


def ad_scheduled_job():
    """Метод расписания CRON. Позволяет запускать анализ объявлений по ссылке из задачи."""
    tasks = models.Task.objects.filter(active=True)    #Поиск активных задач (выводит список)

    for task in tasks:                                 # Перебор задачи
        link = f'{task.url}&sort_by=add_date-asc'      # Взять ссылку задачи и добавить фильтр "По дате"
        ad_list = handler_ads.start(link, task.id, 1)  # Обработка ссылки и получение готовых, новых объявлений
 
        if ad_list:                                    # Если список не пуст и есть хоть что-то...
            email.send(ad_list, task.email)            # Обработать и отправить почтой новые объявления

        for ad in ad_list:                             # Перебрать весь список с новыми объявлениями для лога
            print(ad)                                  # Печать в лог файле (Логирование отключенно
