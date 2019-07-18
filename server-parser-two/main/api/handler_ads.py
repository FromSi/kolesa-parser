from .utils import parser_bot
from . import models


def start(url, task_id, def_page):
    """Поиск новых объявлений с использование БД."""
    ads = parser_bot.get_ads(url, 1)              # Получить со страниц(-ы) все объявления [[1 стр объявлений], [2 стр], ..]
    ad_list = []                                  # Пустой список для новых объявлений

    for ads_list in ads:                          # Получить объявления страницы
        for ad in ads_list:                       # Получить объявление из списка объявлений
            # Если объявления по такому ID, у такой ID задачи нет - объявление новое
            if not models.Ad.objects.filter(uid=ad['id'], task__id=task_id).exists():
                ad_list.append(ad)                # Добавить в конец новое объявление
                new_ad = models.Ad(               # Создать модель объявления в БД
                    uid=ad['id'],                 # Добавить ID объявления по UID, не ID в значение таблицы
                    task_id=task_id               # Добавить ID задачи
                )
                new_ad.save()                     # Сохранить новое объявление в моделе БД

    return ad_list                                # Возвратить новые объявления в виде одного списка
