import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
import codecs

 
def _get_html(link):
    """Получить HTML страницу."""
    response = requests.get(link)
    return response.text


def _get_links(html, link, def_page):
    links = []
    numbers = int(_get_numbers_page(html, def_page))

    for i in range(numbers):
        links.append(f'{link}&page={i + 1}')

    return links


def _get_numbers_page(html, def_page):
    """Получить количество страниц."""
    soup = BeautifulSoup(html, 'lxml')
    spans = soup.find('div', {'class': 'pager'}).find('ul').findAll('span')
    numbers = _get_list_numper_page(spans, def_page)
    
    return numbers


def _get_list_numper_page(spans, def_page):
    """Вычисление количества страниц."""
    if len(spans) <= def_page:
        return len(spans) if len(spans) > 0 else 1
    else:
        return def_page


def _get_ads(html):
    """Получить все объявения."""
    soup = BeautifulSoup(html, 'lxml')
    divs = soup.findAll('div', {'class': 'row vw-item list-item a-elem'})
    ads = list(map(_get_ad_info, divs))
    
    return ads


def _get_ad_info(body):
    """Получение информации объявления."""
    price = body.find('div', {'class': 'a-info-top'}).find('span', {'class': 'price'})
    price.span.decompose()

    return {
        'id': body.get('data-id'),
        'picture': _get_pictures(body),
        'title': body.find('div', {'class': 'a-info-top'}).find('span', {'class': 'a-el-info-title'}).text,
        'price': price.text.replace(" ", "").replace("\xa0", "").replace("\n", ""),
        'description': body.find('div', {'class', 'a-search-description'})
                           .text
                           .replace("\n                        ", "")
                           .replace("\n                    ", "")
                           .replace("\n", ""),
        'city': body.find('div', {'class', 'a-info-bot'})
                    .find('div', {'class', 'list-region'})
                    .text
                    .replace(" ", "")
                    .replace("\n", ""),
        'date': body.find('span', {'class', 'date'}).text
    }


def _get_pictures(body):
    """Получение фотографий машин в списке - ссылки."""
    return list(map(_get_link_picture, body.findAll('picture')))


def _get_link_picture(body):
    """Получить ссылку фотографии с тэга."""
    if body.find('img').get('src') != '':
        if body.find('img').get('src')[0:4] == 'http':
            return body.find('img').get('src')
    else:
        return body.find('img').get('data-url')


def _make_all(link):
    """Получить объявления с определенной страницы."""
    page = _get_html(link)
    ads = _get_ads(page)

    return ads


def _job(link, def_page):
    """Тело алгоритма."""
    ads = []
    links = _get_links(_get_html(link), link, def_page)

    with Pool(40) as p:
        ads += p.map(_make_all, links)

    return ads


def get_ads(link, def_page):
    """Запуск алгоритма."""
    return _job(link, def_page)