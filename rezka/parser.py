import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt

HOST = "https://rezka.ag/"
URL = "https://rezka.ag/page/2/"

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
}


@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req

@csrf_exempt
def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='b-content__inline_items')
    films = []

    for item in items:
        films.append(
            {
                #'title': item.find('img', class_='title-box-2').get_text(strip=True),
                'title': item.find('div', class_='b-content__inline_item-link').get_text(strip=True),#('img')['alt'],
                'image': HOST + item.find('div', class_='b-content__inline_item-cover').find('img').get('src')
            })
    print(films)
    return films

@csrf_exempt
def films_parser():
    html = get_html(URL)
    if html.status_code == 200:
        films = []
        for page in range(0, 1):
            html = get_html(URL, params={'page': page})
            films.extend(get_content(html.text))
            return films
    else:
        raise ValueError('Error in FILMS PARSER')