from . import models, handler_ads
from .utils import email


def ad_scheduled_job():
    profiles = models.Profile.objects.filter(active=True)

    for profile in profiles:
        ad_list = handler_ads.start(profile, 1)

        email.send(ad_list, profile.email)

        for ad in ad_list:
            print(ad)