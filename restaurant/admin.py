from django.contrib import admin

from restaurant.models import Restaurant, RestaurantUser


# Register your models here.
class RestaurantAdmin(admin.ModelAdmin):
    list_display = (
        "uid",
        "name",
        "address",
        "opening_hours",
    )


admin.site.register(Restaurant, RestaurantAdmin)


class RestaurantUserAdmin(admin.ModelAdmin):
    search_fields = ["user__name", "user__phone_number"]


admin.site.register(RestaurantUser, RestaurantUserAdmin)
