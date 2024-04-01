from django.contrib import admin
from .models import Stall
# Register your models here.
class StallAdmin(admin.ModelAdmin):
    model = Stall

# Register your models here.

admin.site.register(Stall, StallAdmin)