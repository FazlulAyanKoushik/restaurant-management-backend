from rest_framework.generics import (
    CreateAPIView,
    UpdateAPIView,
    RetrieveAPIView,
)
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .models import Restaurant
from .serializers import RestaurantSerializer


class RestaurantCreate(CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAdminUser]


class RestaurantRetrieve(RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "uid"


class RestaurantUpdate(UpdateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAdminUser]
    lookup_field = "uid"
    http_method_names = ["put", "patch"]
