from django.contrib import admin

from .models import Interview, Tag


@admin.register(Tag)
class TagManagerAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "created_at"]
    search_fields = ["title", "description"]
    list_filter = ["created_at"]
    prepopulated_fields = {"slug": ("title",)}
    list_per_page = 25


@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    list_display = ["user", "title", "approve", "created_at"]
    list_filter = ["approve"]
    search_fields = ["user", "title"]
    list_per_page = 25
    list_editable = ["approve"]
