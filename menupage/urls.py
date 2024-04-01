# <appname>/urls.py
from django.urls import path
from . import views
from .views import index, menu
urlpatterns = [
    path('', views.index, name='index'),
    path('menu/<str:vendor_key>/', views.menu, name='menu'),
]
# This might be needed, depending on your Django version
menupage = "menupage"
