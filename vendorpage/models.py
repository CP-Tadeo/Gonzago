from asyncio.windows_events import NULL
from django.db import models
from loginpage import models as loginpage_models


# Create your models here.

class Vendor(models.Model):
    vendor_name = models.CharField(max_length=30, default="")
    referenceKey = models.CharField(max_length=30, default="")
    passWord = models.CharField(max_length=30, default="")
    gcashLink = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.vendor_name

class Food_Item(models.Model):
    item_name = models.CharField(max_length=30, default="")
    item_desc = models.TextField(max_length=255, default="")
    item_cost = models.IntegerField(default=0)
    item_avail = models.BooleanField(default=False)
    vendorOwner = models.ForeignKey(Vendor, default=NULL, on_delete=models.CASCADE)

    def __str__(self):
        return self.item_name
    
    def unavail(self):
        self.item_avail = False

    def avail(self):
        self.item_avail = True

class VendorProfile(models.Model):
    stall_name = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True,blank=True)
    stall_desc = models.CharField(max_length=255, default="") #stall description can/SHOULD be done on vendorpage. 
    stall_availability = models.BooleanField(default=True) #Same with this
    stall_image = models.ImageField(null=True, blank=True) #Also this

    
    def __str__(self):
        return str(self.stall_name)
    
    @property
    def imageURL(self):
        try:
            url = self.stall_image.url
        except:
            url = ''
        return url

#class Vendor(models.Model):
#    id = models.BigIntegerField(primary_key=True)
    #stall = models.ForeignKey(Stall, default=NULL, on_delete=models.CASCADE)

#    def __str__(self):
#        return self.name