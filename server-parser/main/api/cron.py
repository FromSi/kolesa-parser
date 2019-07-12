from . import models
from .utils import parser_bot


def ad_scheduled_job():
    profiles = models.Profile.objects.filter(active=True)

    for profile in profiles:
        ads = parser_bot.get_ads(profile.url)
        ad_list = []

        for ads_list in ads:
            for ad in ads_list:
                # print(not models.Ad.objects.filter(id=ad['id']).exists())
                if not models.Ad.objects.filter(id=ad['id']).exists():
                    ad_list.append(ad)

                    new_ad = models.Ad(
                        id=ad['id'],
                        title=ad['title'],
                        price=ad['price'],
                        description=ad['description'],
                        city=ad['city'],
                        date=ad['date'],
                        views= ad['views']
                    )

                    new_ad.save()

                    for picture in ad['picture']:
                        p = models.Picture(
                            url=picture,
                            ad=new_ad
                        )
                        p.save()

        print(ad_list)
        # print(ads)