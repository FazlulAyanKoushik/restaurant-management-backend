from django.urls import path
from . import views

urlpatterns = [
    path(
        "",
        views.RestaurantCreate.as_view(),
        name="restaurant-create",
    ),
    path(
        "/<uuid:uid>",
        views.RestaurantRetrieve.as_view(),
        name="restaurant-retrieve",
    ),
    path(
        "/<uuid:uid>/update",
        views.RestaurantUpdate.as_view(),
        name="restaurant-update",
    )
    # Add other URLs if needed
]
