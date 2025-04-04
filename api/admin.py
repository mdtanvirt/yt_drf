from django.contrib import admin
from .models import Product, Order, OrderItem

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    search_field = ('name', 'price')

admin.site.register(Order)
admin.site.register(OrderItem)