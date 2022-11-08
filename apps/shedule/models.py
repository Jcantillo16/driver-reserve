from django.db import models


class Shedule(models.Model):
    collection_date = models.DateField()
    collection_time = models.TimeField()
    order = models.ForeignKey("orders.Order", on_delete=models.CASCADE, blank=True, null=True,
                              related_name='order_shedule')

    def __str__(self):
        shedule = "Shedule: " + str(self.collection_date) + " - " + str(self.collection_time)
        return shedule

    class Meta:
        db_table = 'shedule'
