from django.contrib import admin

from .models import User, Profile


class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "is_active"]
    list_filter = ["is_active"]
    search_fields = ["username", "email"]
    list_per_page = 25


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "twitter", "instagram", "telegram"]
    search_fields = ["user", "twitter", "instagram"]
    list_per_page = 25


admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
