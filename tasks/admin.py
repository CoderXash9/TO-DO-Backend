from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "priority",
        "status",
        "due_date",
        "created_at",
    )

    search_fields = (
        "title",
        "description",
    )

    list_filter = (
        "priority",
        "status",
        "due_date",
    )

    ordering = ("due_date",)

    list_per_page = 10
