import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt

HOST = "https://animekisa.tv"
URL = "https://animekisa.tv/latest/1"

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
    items = soup.find_all('div', class_='episode-box test')
    anime = []

    for item in items:
        anime.append(
            {
                'title': item.find('div', class_='title-box-2').get_text(strip=True),
                'image': HOST + item.find('div', class_='image-box').find('img').get('src')
            })
    print(anime)
    return anime

@csrf_exempt
def anime_parser():
    html = get_html(URL)
    if html.status_code == 200:
        anime = []
        for page in range(0, 1):
            html = get_html(URL, params={'page': page})
            anime.extend(get_content(html.text))
            return anime
    else:
        raise ValueError('Error in ANIME PARSER')