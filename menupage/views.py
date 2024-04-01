from django.shortcuts import render, redirect
from django.http import HttpResponse
from vendorpage.models import Food_Item
from vendorpage.models import VendorProfile
from vendorpage.models import Vendor

def index(request):
    stall_list = VendorProfile.objects.order_by("stall_availability")
    food_list = Food_Item.objects.order_by("item_name")
    return render(request, 'menupage/detail.html', {"stall_list": stall_list,"food_list": food_list})


def menu(request, vendor_key):
    # Get the vendor object
    vendor = Vendor.objects.get(referenceKey=vendor_key)
    # Get all stalls for this vendor
    stalls = VendorProfile.objects.filter(stall_name=vendor)
    # Get all food items for this vendor
    food_list = Food_Item.objects.filter(vendorOwner=vendor).order_by("item_name")
    context = {
        'vendor': vendor,
        'stalls': stalls,
        "food_list": food_list
    }
    return render(request, 'menupage/detail.html', context)

