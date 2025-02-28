import os
from main.models import Films

def imagedr():
    image_dir = os.path.join('films')
    name_img = os.listdir(image_dir)
    full_name_img = list()
    for i in name_img:
        chenge = '/films/' + i
        full_name_img.append(chenge)
        for text in full_name_img:
            number = ''
            for j in text:
                if j.isdigit():
                    number+=j
            num = int(number)
            new_images = Films.objects.get(id=num)
            new_images.image = text
            new_images.save()

