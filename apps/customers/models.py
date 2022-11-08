from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    key = models.TextField(max_length=200, blank=True, null=False)
    is_logged = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'customers'
