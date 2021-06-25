from django.contrib import admin
from .models import Box, Activity, Category, Reason
from django.contrib import admin
"""from foo.models import Permission
from django_extensions.admin import ForeignKeyAutocompleteAdmin"""

# Register your models here.
admin.site.register(Box)
admin.site.register(Activity)
admin.site.register(Category)
admin.site.register(Reason)


""" class PermissionAdmin(ForeignKeyAutocompleteAdmin):
    # User is your FK attribute in your model
    # first_name and email are attributes to search for in the FK model
    related_search_fields = {
        'user': ('first_name', 'email'),
    }

    fields = ('user', 'avatar', 'is_active')

    ...


admin.site.register(Permission, PermissionAdmin)"""
