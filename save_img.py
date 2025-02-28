from http.client import responses
import requests
from http.client import responses
from types import new_class

import requests
from bs4 import BeautifulSoup


def images(url) -> list:
    all_img = list()
    chen = 1
    for i in range(1, 21):
        response = requests.get(url + '?page=' + str(i))
        image_data = BeautifulSoup(response.content, 'lxml')
        img_tag = image_data.find_all('img')
        c=0
        for j in img_tag:
            if c>1 and c<52:
                img_src = j.get('src')
                all_img.append(img_src)
            c+=1
    return all_img
url = 'https://kino.mail.ru/cinema/all/'

def get_img(mass: list):
    c = 1
    s = requests.Session()
    for img in mass:
        path = 'code_geass' + str(c) + '.jpg'
        r = s.get(img)
        if r.status_code == 200:
            print(img)
            with open(f'films\\{path}', 'wb') as f:
                f.write(r.content)
                print(path)
        c +=1
get_img(images(url))
print(images(url))