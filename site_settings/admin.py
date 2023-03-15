from django.contrib import admin
from site_settings.models import *


class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag']
    readonly_fields = ['image_tag']


class ContactDataAdmin(admin.ModelAdmin):
    list_display = ['phone1', 'phone2', 'email']


admin.site.register(About, AboutAdmin)
admin.site.register(ContactData, ContactDataAdmin)
admin.site.register(TelegramBot)
admin.site.register(HomeSlider)
