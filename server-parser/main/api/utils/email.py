from django.core.mail import send_mail


def send(ads, email):
    text = 'Привет! Мы для Вас нашли новые объявления!\n'

    for ad in ads:
        imgs = ''
        text += '\n'
        text += f'Ссылка: https://kolesa.kz/a/show/{ad["id"]}\n'
        text += f'Заголовок: {ad["title"]}\n'
        text += f'Описание: {ad["description"]}\n'
        text += f'Город: {ad["city"]}\n'
        text += f'Цена: {ad["price"]}\n'
        text += f'Дата: {ad["date"]}\n'

        for img in ad["picture"]:
            imgs += f'\n\t{img}'

        text += f'Изображение(-я): {imgs}\n-----\n'

    send_mail(
        'Новыe объявления',
        text,
        'fromsitest@yandex.com',
        [email],
        fail_silently=False,
    )
