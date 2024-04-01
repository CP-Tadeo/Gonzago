from django.db import models
# Create your models here.

class Stall(models.Model):
    # id = models.BigIntegerField(primary_key=True,default=0)
    name = models.CharField(max_length=30, default="")
    referenceKey = models.CharField(max_length=30, default="")
    passWord = models.CharField(max_length=30, default="")

    def __str__(self):
        return self.name