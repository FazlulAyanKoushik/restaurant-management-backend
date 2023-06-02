from django.contrib import admin
from accounts.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    search_fields = ["email", "phone_number"]
    list_filter = ["is_active", "is_superuser"]

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Personal Info",
            {
                "fields": (
                    "name",
                    "phone_number",
                )
            },
        ),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Important dates", {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "phone_number",
                    "name",
                ),
            },
        ),
    )

    list_display = [
        "email",
        "name",
        "phone_number",
        "is_active",
        "is_staff",
        "is_superuser",
    ]
    ordering = ["email"]


admin.site.register(User, UserAdmin)
