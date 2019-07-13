from .utils import parser_bot
from . import models


def start(profile, def_page):
    ads = parser_bot.get_ads(profile.url, 1)
    ad_list = []

    for ads_list in ads:
        for ad in ads_list:
            if not models.Ad.objects.filter(uid=ad['id']).exists():
                ad_list.append(ad)
                new_ad = models.Ad(
                    uid=ad['id'],
                    title=ad['title'],
                    price=ad['price'],
                    description=ad['description'],
                    city=ad['city'],
                    date=ad['date']
                )
                new_ad.save()

                for picture in ad['picture']:
                    p = models.Picture(
                        url=picture,
                        ad=new_ad
                    )
                    p.save()

                profile.ad.add(new_ad)
            else:
                if not profile.ad.all().filter(uid=ad['id']).exists():
                    ad_list.append(ad)
                    old_ad = models.Ad.objects.get(uid=ad['id'])
                    profile.ad.add(old_ad)

    return ad_list