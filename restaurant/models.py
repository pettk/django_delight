from django.db import models

# Create your models here.
class Inventory(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.FloatField()
    price_per_unit = models.FloatField()

    def __str__(self):
        return self.name
