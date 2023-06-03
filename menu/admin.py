from django.contrib import admin
from .models import Menu, MenuRestaurantConnector


# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    search_fields = ["name"]


admin.site.register(Menu, MenuAdmin)


class MenuRestaurantConnectorAdmin(admin.ModelAdmin):
    search_fields = ["restaurant__name"]


admin.site.register(MenuRestaurantConnector, MenuRestaurantConnectorAdmin)
