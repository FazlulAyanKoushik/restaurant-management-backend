from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth import get_user_model
from rest_framework.exceptions import APIException

from core.models import BaseModelWithUID

User = get_user_model()


# Create your models here.
class Restaurant(BaseModelWithUID):
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=200)
    description = models.TextField()
    opening_hours = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk and Restaurant.objects.exists():
            raise APIException("Only one restaurant can be created.")
        try:
            return super().save(*args, **kwargs)
        except ValidationError as e:
            raise APIException(str(e))


class RestaurantUser(BaseModelWithUID):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="staff_members"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="employed_restaurants",
    )

    class Meta:
        unique_together = ("restaurant", "user")

    def __str__(self):
        return f"{self.user.name} employee of {self.restaurant.name}"
