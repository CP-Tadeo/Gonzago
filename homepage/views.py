from django.shortcuts import render
from django.http import HttpResponse
from vendorpage import models as vendorpage_models
from .models import *

def index(request):
    context = {}
    return render(request, 'homepage/detail.html', context)
#    return HttpResponse('Hello World! This came from the index view')

#views gets it data from vendorpage models, not from itselfs models. 

# def stall_list(request):
#     #stalls = Stall.objects.all() #FIX LATER
#     stalls = vendorpage_models.VendorProfile.objects.all().order_by('stall_name')
#     context = {'stalls':stalls}
#     return render(request, "homepage/homepage.html", context)from vendorpage.models import VendorProfile

def stall_list(request):
    stalls = vendorpage_models.VendorProfile.objects.all().order_by('stall_name__vendor_name')

    context = {'stalls': stalls}
    return render(request, "homepage/homepage.html", context)


