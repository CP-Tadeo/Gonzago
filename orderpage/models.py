from django.db import models

from vendorpage.models import Vendor, Food_Item

# Create your models here.
class Item(models.Model):
    item = models.ForeignKey(
        Food_Item,
        on_delete = models.SET_NULL,
        blank = True,
        null = True
    )
    @property
    def price(self):
        return self.item.item_cost

    pass

class Order(models.Model):
    refNumber = models.IntegerField()
    vendor = models.ForeignKey(
        Vendor,
        on_delete = models.SET_NULL,
        blank = True,
        null = True
    )
    @property
    def gCash (self):
        return self.vendor.gcashLink

    items = models.ManyToManyField(Item)
    
    @property
    def total_price (self):
        price = 0
        for i in range(len(self.items)):
            price += self.items[i].price(self)

        return price
