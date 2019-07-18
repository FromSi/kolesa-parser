from . import models, handler_ads
from .utils import email


def ad_scheduled_job():
    tasks = models.Task.objects.filter(active=True)

    for task in tasks:
        ad_list = handler_ads.start(task.url, task.id, 1)

        if ad_list:
            email.send(ad_list, task.email)

        for ad in ad_list:
            print(ad)
