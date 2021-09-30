import requests
from bs4 import BeautifulSoup
import csv
import os

url = 'https://carloson.ru/car'
host = 'https://carloson.ru/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    '(KHTML, like Gecko) Chrome/92.0.4515.159 YaBrowser/21.8.3.614 Yowser/2.5 Safari/537.36'
}
path = 'carloson.csv'


def get_html(url):
    r = requests.get(url, headers=headers)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('a', class_='col-xl-4 col-lg-4 col-md-6 col-sm-6 col-12 mb-2 mb-md-4')
    cards = []
    for item in items:
         cards.append({
             'title': item.find('p', class_='two__block_slide__text__name').get_text().replace(' ', '').replace('\n', ''),
             'specifications': item.find('div', class_='two__block_slide__text__bottom').get_text().replace(' ', '').replace('\n', ' ').strip().replace('₽', 'Р'),
             'link': item.get('href'),
             'img': item.find('div', class_='img__box').find('img').get('data-src'),
         })

    return cards


def save_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название', 'Характеристики', 'Ссылка', 'Картинка'])
        for item in items:
            writer.writerow([item['title'], item['specifications'], item['link'], item['img']])


def parse():
    html = get_html(url)
    if html.status_code == 200:
        cards = get_content(html.text)
        save_file(cards, path)
        os.startfile(path)


parse()