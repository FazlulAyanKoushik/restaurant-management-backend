from django.db import models

from core.models import BaseModelWithUID


# Create your models here.
class Menu(BaseModelWithUID):
    restaurant = models.ForeignKey("Restaurant", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name
