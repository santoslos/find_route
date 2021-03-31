from django.db import models
from django.urls import reverse


class City(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = "Города"
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('cities:detail', kwargs={'pk_city': self.pk})

    def get_absolute_url_update(self):
        return reverse('cities:update', kwargs={'pk_city': self.pk})

    def get_absolute_url_delete(self):
        return reverse('cities:delete', kwargs={'pk_city': self.pk})
