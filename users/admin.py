from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "city", "date_joined")
    search_fields = ("email", "city")
    ordering = ("-date_joined",)
