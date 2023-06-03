from rest_framework import serializers
from django.contrib.auth import get_user_model

from restaurant.models import Restaurant, RestaurantUser

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    restaurant_uid = serializers.SlugRelatedField(
        queryset=Restaurant.objects.filter(), slug_field="uid", write_only=True
    )
    password = serializers.CharField(write_only=True)
    name = serializers.CharField(max_length=13, required=False)
    phone_number = serializers.CharField(max_length=13, required=False)

    class Meta:
        model = User
        fields = ("email", "password", "phone_number", "name", "restaurant_uid")

    def create(self, validated_data):
        name = validated_data.get("name", "")
        phone_number = validated_data.get("phone_number", "")
        restaurant = validated_data.pop("restaurant_uid", None)

        user = User.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            phone_number=phone_number,
            name=name,
        )

        RestaurantUser.objects.create(restaurant=restaurant, user=user)

        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get("email", instance.email)
        instance.set_password(validated_data.get("password", instance.password))
        instance.name = validated_data.get("name", instance.name)
        instance.phone_number = validated_data.get(
            "phone_number", instance.phone_number
        )
        instance.save()

        return instance
