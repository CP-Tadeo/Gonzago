# <appname>/urls.py
from django.urls import path
from .views import log_in
from .views import page_not_found

urlpatterns = [
    path('', page_not_found, name='Page Not Found')
    #path('', log_in, name='Log In'),
    #path('login/', log_in_attempt, name='Log In Attempt'),
]
# This might be needed, depending on your Django version
loginpage = "loginpage"