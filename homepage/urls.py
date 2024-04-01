# <appname>/urls.py
from django.urls import path
from . import views
from .views import index
urlpatterns = [
    #path('', index, name='index'),
    path('', views.stall_list, name="stalls"),
]
# This might be needed, depending on your Django version
homepage = "homepage"