from django.contrib.auth import get_user_model

from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer

User = get_user_model()


class UserRegistration(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PrivateUserUpdate(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
