from django.db import models
class Task(models.Model):
    title = models.CharField('Название', max_length = 50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

class Films(models.Model):
    name = models.CharField(max_length = 500, blank = False)
    teges = models.CharField(max_length = 500, blank=False)
    image = models.ImageField(blank=True, upload_to='films')
    def __str__(self):
        return self.name

