from django.db import models


# Create your models here.


class Driver(models.Model):
    name = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'drivers'


class LocationDriver(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='location')
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True, default='Colombia')
    lat = models.FloatField(default=0)
    lng = models.FloatField(default=0)
    lastUpdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'location_drivers'
