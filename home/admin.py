from django.contrib import admin
from home.models import *


class ProductImageInline(admin.TabularInline):
    model = ImageItem
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'image_tag']
    readonly_fields = ['id', 'create_at']
    inlines = [ProductImageInline]


class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone']
    readonly_fields = ['first_name', 'last_name', 'phone', 'message', 'ip', 'create_at']


admin.site.register(Product, ProductAdmin)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Category)
admin.site.register(User)
