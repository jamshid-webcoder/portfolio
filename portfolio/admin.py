from django.contrib import admin
from .models import Contact

# Register your models here.
admin.site.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'title')
    search_fields = ('name', 'email')
    ordering = ('name')
    list_filter = ('name', 'email')

    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'title', 'message')
        }),
    )