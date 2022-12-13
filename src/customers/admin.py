from django.contrib import admin

from src.customers.models import Profile, Technology


class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid', 'modified', 'created')
    search_fields = ['first_name', 'last_name']
    list_display = ('first_name', 'last_name', 'contacts')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Technology)
