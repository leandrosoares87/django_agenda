from django.contrib import admin
from contact.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'fist_name', 'last_name', 'phone',
    ordering = '-id',
    list_filter = 'created_date',
    search_fields = 'fist_name', 'last_name', 'phone',
    list_per_page = 1
    list_max_show_all = 200
    list_editable = 'last_name', 'phone'
    list_display_links = 'id', 'fist_name',
