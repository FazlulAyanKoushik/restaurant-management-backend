from rest_framework import serializers
from restaurant.models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ("uid", "name", "address", "description", "opening_hours")
        read_only_fields = ("uid",)


class PrivateEmployeeSlimSerializer(serializers.Serializer):
    uid = serializers.UUIDField(source="user.uid", read_only=True)
    name = serializers.UUIDField(source="user.name", read_only=True)
    email = serializers.UUIDField(source="user.email", read_only=True)
    phone_number = serializers.UUIDField(source="user.phone_number", read_only=True)


class PrivateRestaurantEmployeeSerializer(serializers.ModelSerializer):
    employee_list = PrivateEmployeeSlimSerializer(
        source="staff_members", many=True, read_only=True
    )

    class Meta:
        model = Restaurant
        fields = ("uid", "name", "employee_list")
        read_only_fields = ("__all__",)
