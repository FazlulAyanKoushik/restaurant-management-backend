from django.urls import path
from . import views

urlpatterns = [
    path(
        "",
        views.MenuListCreateAPIView.as_view(),
        name="menu-create",
    ),
    path(
        "/<uuid:uid>",
        views.MenuRetrieveUpdateDestroyAPIView.as_view(),
        name="menu-detail",
    ),
]
