from django.contrib import admin

from src.mail.models import Mail


class MailAdmin(admin.ModelAdmin):
    readonly_fields = ('email',)
    search_fields = ['email',]
    list_display = ('email',)


admin.site.register(Mail, MailAdmin)
