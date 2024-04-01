from django.db import models
from vendorpage import models as vendorpage_model

# Create your models here.
#As of 12:08 am, 04-11-23, technically not needed any more
class Stall(models.Model):
    stall_name = models.ForeignKey(vendorpage_model.Vendor, on_delete=models.SET_NULL, null=True,blank=True)
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