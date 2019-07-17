from .utils import parser_bot
from . import models


def start(url, task_id, def_page):
    ads = parser_bot.get_ads(url, 1)
    ad_list = []

    for ads_list in ads:
        for ad in ads_list:
            if not models.Ad.objects.filter(uid=ad['id'], task__id=task_id).exists():
                ad_list.append(ad)
                new_ad = models.Ad(
                    uid=ad['id'],
                    task_id=task_id
                )
                new_ad.save()

    return ad_list