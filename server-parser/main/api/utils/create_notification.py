def _get_url(url_base, **kwargs):
    """Получить ссылку.
    
    Ключи для **kargs:
    model -- модель машины (спец символы модели)
    mark -- марка машины (спец символы марки)
    type -- тип машины (спец символы типа)
    city -- город (спец символы города)
    price_from -- цена от (указывать цену)
    price_to -- цена до (указывать цену)
    photo -- c фото (Значения не важны)
    torg -- срочно, торг (Значения не важны)
    auto_custom -- растаможен (Значения не важны)
    """
    url = url_base
    first_symbol = False

    url += 'cars/' 
    url += kwargs['mark'] + '/' if kwargs['mark'] != None else ''
    url += kwargs['model'] + '/' if kwargs['model'] != None else ''

    if kwargs['type'] != None:
        url += '&' if first_symbol else '?'
        url += f'auto-car-grbody={kwargs["type"]}'

    if kwargs['city'] != None:
        url += '&' if first_symbol else '?'
        url += f'region={kwargs["city"]}'

    if kwargs['price_from'] != None:
        url += '&' if first_symbol else '?'
        url += f'price[from]={kwargs["price_from"]}'

    if kwargs['price_to'] != None:
        url += '&' if first_symbol else '?'
        url += f'price[to]={kwargs["price_to"]}'

    if kwargs['photo'] != None:
        url += '&' if first_symbol else '?'
        url += '_sys-hasphoto=2'

    if kwargs['torg'] != None:
        url += '&' if first_symbol else '?'
        url += '_sys-torg=1'

    if kwargs['auto_custom'] != None:
        url += '&' if first_symbol else '?'
        url += 'auto-custom=2'

    url += '&sort_by=add_date-asc' if first_symbol else '?sort_by=add_date-asc'

    return url


def create(data, profile, mark, t, city):
    """Создать уведомление.
    
    Ключи для **kargs:
    model -- марка машины (спец символы марки)
    mark -- марка машины (спец символы марки)
    type -- тип машины (спец символы типа)
    city -- город (спец символы города)
    price_from -- цена от (указывать цену)
    price_to -- цена до (указывать цену)
    photo -- c фото (Значения не важны)
    torg -- срочно, торг (Значения не важны)
    auto_custom -- растаможен (Значения не важны)
    """
    url = _get_url(
        'https://kolesa.kz/', 
        model=data.get('model'),
        mark=data.get(mark),
        type=data.get(t),
        city=data.get(city),
        price_from=data.get('price_from'),
        price_to=data.get('price_to'),
        photo=data.get('photo'),
        torg=data.get('torg'),
        auto_custom=data.get('auto_custom'),
    )

    profile.url = url
    profile.save()