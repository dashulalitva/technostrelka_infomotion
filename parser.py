from http.client import responses
from types import new_class

import requests
from bs4 import BeautifulSoup

from main.models import Films


def images(url):
    chen = 1
    for i in range(1, 21):
        response = requests.get(url + '?page=' + str(i))
        image_data = BeautifulSoup(response.content, 'lxml')
        img_tag = image_data.find_all('img')
        c=0
        for j in img_tag:
            if c>1 and c<52:
                img_src = j.get('src')
                img_to_change = Films.objects.get(id=chen)
                img_to_change.image = img_src
                img_to_change.save()
                chen+=1
            c+=1
url = 'https://kino.mail.ru/cinema/all/'
for i in range(1, 21):
    images(url + '?page=' + str(i))


def film_name(url):
    chen = 1
    for i in range(1, 21):
        response = requests.get(url + '?page=' + str(i))
        data = BeautifulSoup(response.text, 'lxml')
        film_data = data.find_all('div', class_='p-itemevent-small__info')
        c=0
        for i in film_data:
            if c%2==0:
                name = i.find('span', class_='link__text').text
                teg = i.find('div', class_='margin_top_5').text.split(', ')
                new_data = Films.objects.get(id=chen)
                new_data.name = name
                new_data.teges = teg
                new_data.save()
                chen += 1
            c+=1
url = 'https://kino.mail.ru/cinema/all/'

