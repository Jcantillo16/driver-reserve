from django.db import models
from apps.customers.models import Customer


class PaymentMethod(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'payment_method'


class Payment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer')
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE, related_name='payment_method')
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE, related_name='order', null=True)
    value = models.FloatField()
    date = models.DateField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.value

    class Meta:
        db_table = 'payment'
