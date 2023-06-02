from django.urls import path


from accounts import views

app_name = "user"

urlpatterns = [
    path("/register", views.UserRegistration.as_view(), name="registration"),
    path("", views.PrivateUserUpdate.as_view(), name="registration"),
]
