from rest_framework import serializers
from menu.models import Menu, MenuRestaurantConnector


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ("uid", "name", "price", "description")
        read_only_fields = ("uid",)

    def create(self, validated_data):
        user = self.context.get("request").user
        restaurant = user.employed_restaurants.filter().first().restaurant

        menu = Menu.objects.create(**validated_data)
        MenuRestaurantConnector.objects.create(restaurant=restaurant, menu=menu)
        return menu

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.price = validated_data.get("price", instance.price)
        instance.save()

        return instance
