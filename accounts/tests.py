from django.contrib.auth import get_user_model

from rest_framework.test import APIClient, APITestCase

User = get_user_model()


class UserModelTestCase(APITestCase):
    def setUp(self):
        self.user_data = {
            "email": "test@example.com",
            "password": "password123",
        }

    def test_create_user(self):
        user = User.objects.create_user(**self.user_data)

        self.assertEqual(user.email, self.user_data["email"])
        self.assertTrue(user.is_active)

    def test_create_superuser(self):
        superuser = User.objects.create_superuser(**self.user_data)

        self.assertEqual(superuser.email, self.user_data["email"])
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)

    def test_str_representation(self):
        user = User.objects.create_user(**self.user_data)
        self.assertEqual(str(user), self.user_data["email"])
