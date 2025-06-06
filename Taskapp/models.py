from django.db import models

class SalesRecord(models.Model):
    region = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    item_type = models.CharField(max_length=100)
    sales_channel = models.CharField(max_length=50)
    order_priority = models.CharField(max_length=1)
    order_date = models.DateField()
    order_id = models.IntegerField(unique=True)
    ship_date = models.DateField()
    units_sold = models.IntegerField()
    unit_price = models.FloatField()
    unit_cost = models.FloatField()
    total_revenue = models.FloatField()
    total_cost = models.FloatField()
    total_profit = models.FloatField()

    def __str__(self):
        return f"{self.order_id} - {self.country} - {self.item_type}"
