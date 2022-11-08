from django.db import models
from apps.customers.models import Customer
from apps.payment.models import Payment
from apps.shedule.models import Shedule
from apps.drivers.models import Driver
from geopy.geocoders import Nominatim


class Status_Order(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'status_order'


class Type_Order(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'type_order'


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.ForeignKey(Status_Order, on_delete=models.CASCADE, related_name='status', default=1)
    type_order = models.ForeignKey(Type_Order, on_delete=models.CASCADE, related_name='type_order')
    address = models.CharField(max_length=100, )
    description = models.TextField(max_length=200, blank=True, null=False)
    shedule = models.ForeignKey(Shedule, on_delete=models.CASCADE, related_name='shedule')
    package_value = models.FloatField()
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='payment')
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='driver', blank=True, null=True)

    def __str__(self):
        order = "Order: " + str(self.id) + " - " + self.customer.name
        return order

    class Meta:
        db_table = 'orders'


class LocationOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='location')
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True, default='Colombia')
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        Location_order = "Location: " + str(self.latitude) + " - " + str(self.longitude)
        return Location_order

    def save(self, *args, **kwargs):
        geolocator = Nominatim(user_agent="my_user_agent")
        location = geolocator.geocode(self.order.address)
        self.latitude = location.latitude
        self.longitude = location.longitude
        self.city = location.address.split(',')[-3]

        if self.latitude < 0:
            self.latitude = self.latitude * -1
        if self.longitude < 0:
            self.longitude = self.longitude * -1

        if self.latitude > 100:
            self.latitude = self.latitude / 10
        if self.longitude > 100:
            self.longitude = self.longitude / 10

        super(LocationOrder, self).save(*args, **kwargs)

    class Meta:
        db_table = 'location_order'
