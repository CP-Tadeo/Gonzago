# <appname>/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.log_in, name='Log In'),
    path('login/', views.log_in_attempt, name='Log In Attempt'),
    path('vendor/', views.vendor_page, name='Vendor Page'),
    path('vendor/', views.vendor_page, name='vendor'),
    path('vendor/u/', views.update_items_vendor_page, name='Update Availability'),
    path('vendor/a/', views.add_new_item, name='Add New Item'),
    path('vendor/add_vendor_profile/', views.add_vendor_profile, name='add_vendor_profile'),
]
# This might be needed, depending on your Django version
vendorpage = "vendorpage"
