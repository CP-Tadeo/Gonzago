from django.contrib import admin
from .models import Order, Item

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    model = Order

class ItemAdmin(admin.ModelAdmin):
    model = Item

admin.site.register(Order, OrderAdmin)
admin.site.register(Item, ItemAdmin)