from django import forms
from django.forms import Textarea

from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'vendor'
            'items'
        ]