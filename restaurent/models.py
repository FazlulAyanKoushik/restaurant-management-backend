from django.db import models

from core.models import BaseModelWithUID

from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Restaurant(BaseModelWithUID):
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=200)
    description = models.TextField()
    opening_hours = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class RestaurantUser(BaseModelWithUID):
    restaurant = models.ForeignKey("Restaurant", on_delete=models.CASCADE)
    user = models.ForeignKey("User", on_delete=models.CASCADE)

    class Meta:
        unique_together = ("restaurant", "user")

    def __str__(self):
        return f"{self.user.name} employee of {self.restaurant.name}"
