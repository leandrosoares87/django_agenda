from django.contrib import admin
from contact import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'fist_name', 'last_name', 'phone', 'show',
    ordering = '-id',
    list_filter = 'created_date',
    search_fields = 'fist_name', 'last_name', 'phone',
    list_per_page = 20
    list_max_show_all = 500
    list_editable = 'last_name', 'phone', 'show',
    list_display_links = 'id', 'fist_name',


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id',
