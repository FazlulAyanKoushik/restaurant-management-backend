# Generated by Django 4.2.1 on 2023-06-03 13:29

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant", "0002_alter_restaurantuser_user"),
        ("menu", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="MenuRestaurantConnector",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uid",
                    models.UUIDField(
                        db_index=True, default=uuid.uuid4, editable=False, unique=True
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "menu",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="menu_restaurants",
                        to="menu.menu",
                    ),
                ),
                (
                    "restaurant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="menu_set",
                        to="restaurant.restaurant",
                    ),
                ),
            ],
            options={
                "unique_together": {("restaurant", "menu")},
            },
        ),
    ]
