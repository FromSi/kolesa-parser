from . import models, handler_ads


def ad_scheduled_job():
    profiles = models.Profile.objects.filter(active=True)

    for profile in profiles:
        ad_list = handler_ads.start(profile, 1)

        for ad in ad_list:
            print(ad)