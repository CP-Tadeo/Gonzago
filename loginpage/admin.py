from django.contrib import admin

from .models import Stall

class StallAdmin(admin.ModelAdmin):
    model = Stall

# Register your models here.

admin.site.register(Stall, StallAdmin)