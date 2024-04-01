from django.contrib import admin


from .models import Vendor, Food_Item, VendorProfile

class VendorAdmin(admin.ModelAdmin):
    model = Vendor
class Food_ItemAdmin(admin.ModelAdmin):
    model = Food_Item

class VendorProfileAdmin(admin.ModelAdmin):
    model = VendorProfile

# Register your models here.

admin.site.register(Vendor, VendorAdmin)
admin.site.register(Food_Item, Food_ItemAdmin)
admin.site.register(VendorProfile, VendorProfileAdmin)