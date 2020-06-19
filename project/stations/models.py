from django.db import models

# Create your models here.

class Route(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'

    def __str__(self):
        return self.name


class Station(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    routes = models.ManyToManyField(Route, related_name='stations')
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Остановка'
        verbose_name_plural = 'Остановки'

    def __str__(self):
        return self.name