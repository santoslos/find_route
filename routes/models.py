from django.db import models

# Create your models here.
from cities.models import City


class Route(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название маршута')
    travel_times = models.PositiveSmallIntegerField(verbose_name="Ощее время в пути")
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='route_from_city_set',
                                  verbose_name='Из какого города')
    to_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='route_to_city_set',
                                verbose_name='В какой город')
    trains = models.ManyToManyField('trains.Train', verbose_name='Список поездов')

    def __str__(self):
        return f' Маршут {self.name} из города {self.from_city} в {self.to_city}'

    class Meta:
        verbose_name = 'Маршут'
        verbose_name_plural = "Маршуты"
        ordering = ['travel_times']