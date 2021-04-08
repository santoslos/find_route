from django.contrib import admin

# Register your models here.
from trains.models import Train

admin.site.register(Train)


class TrainAdmin(admin.ModelAdmin):
    class Meta:
        meta = Train

    list_display = ('name', 'from_city', 'to_city', 'travel_time')



