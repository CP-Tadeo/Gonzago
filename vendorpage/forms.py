from django import forms
from .models import Food_Item, Vendor

class UpdateFoodItemAvailForm(forms.ModelForm):
    class Meta:
        model = Food_Item
        fields = ('item_name','item_avail')
        exclude =  ['item_desc', 'item_cost', 'vendorOwner']

class FoodItemForm(forms.ModelForm):
    class Meta:
        model = Food_Item
        fields = ['item_name', 'item_desc', 'item_cost']

        # def clean(self):
        #     data = self.cleaned_data
        #     item_name = data.get("item_name")
        #     qs = Food_Item.objects.filter(item_name__icontains=item_name)
        #     if qs.exists():
        #         self.add_error("item_name", f"{item_name} already exists.")
        #     return data
from .models import VendorProfile

class VendorProfileForm(forms.ModelForm):
    stall_desc = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'maxlength': 100}))
    stall_availability = forms.ChoiceField(choices=[(True, 'Open'), (False, 'Closed')], widget=forms.Select)
    class Meta:
        model = VendorProfile
        fields = ['stall_desc', 'stall_availability', 'stall_image']
