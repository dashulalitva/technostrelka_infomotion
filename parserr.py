import os

from django.conf import settings

from main.models import Films
from main.parser import images


def parser_database():
    image_dir = os.path.join(settings.MEDIA_ROOT, 'films')
    chen=1
    for filename in os.listdir(image_dir):
        image_path = os.path.join('films1', filename)
        im = Films.objects.get(id=chen)
        im = image_path
        im.save()
        chen+=1
parser_database()