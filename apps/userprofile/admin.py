from django.contrib import admin
from apps.userprofile.models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        "telegram_id",
        "username",
    )
    ordering = ("created_at",)
