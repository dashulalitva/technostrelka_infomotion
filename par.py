from main.models import Films
def jyhg():
    for i in range(1981, 2982):
         gtg = Films.objects.get(id=i)
         gtg.image.delete()