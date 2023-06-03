from django.db import models

from core.models import BaseModelWithUID
from restaurant.models import Restaurant


# Create your models here.
class Menu(BaseModelWithUID):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class MenuRestaurantConnector(BaseModelWithUID):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="menu_set"
    )
    menu = models.ForeignKey(
        Menu,
        on_delete=models.SET_NULL,
        null=True,
        related_name="menu_restaurants",
    )

    class Meta:
        unique_together = ("restaurant", "menu")

    def __str__(self):
        return f"{self.menu.name} menu of {self.restaurant.name}"
