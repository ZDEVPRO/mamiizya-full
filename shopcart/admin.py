from django.contrib import admin
from shopcart.models import *


class OrderInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    can_delete = False
    readonly_fields = ['product', 'title', 'price', 'quantity', 'color', 'size', 'image_tag', 'view_image']
    exclude = ('image',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone_number', 'region']
    readonly_fields = ['user', 'first_name', 'last_name', 'phone_number', 'region', 'district', 'address', 'client_notes', 'id', 'updated_at', 'created_at']
    inlines = [OrderInline]


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'quantity', 'amount', 'image_tag']
    readonly_fields = ['order', 'product', 'title', 'price', 'Jami_Narxi', 'quantity', 'color', 'size', 'image_tag_big', 'view_image']
    exclude = ('image',)


class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['']


admin.site.register(ShopCart)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
