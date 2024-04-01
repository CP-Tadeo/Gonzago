from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Vendor, Food_Item, VendorProfile
from loginpage.views import log_in_attempt
from .forms import FoodItemForm

# Create your views here.
def log_in(request):
    return render(request, 'vendorpage/detail.html')


def log_in_attempt(request):
    message = "Incorrect reference key or password"
    if request.method == "POST":   # IF LOGGING IN
        refKey = request.POST.get("refKey")
        try: # CHECK IF STALL WITH REF KEY EXISTS
            vendor_Obj = Vendor.objects.get(referenceKey=refKey)
        except Vendor.DoesNotExist:
            vendor_Obj = None

        if vendor_Obj: # IF STALL EXISTS
            passWord = request.POST.get("passWord")

            if vendor_Obj.passWord == passWord: # CHECK PASSWORD
                #LOG IN
                request.session["vendor_Ref"] = vendor_Obj.referenceKey
                return redirect('Vendor Page')
            else:
                request.session["vendor_Ref"] = None
                return render(request, 'vendorpage/detail.html',  {'message': message})
        else:
            return render(request, 'vendorpage/detail.html',  {'message': message})

    return render(request, 'vendorpage/detail.html', {'message': message})

def vendor_page(request):
    vendor_Ref = request.session.get('vendor_Ref')
    if vendor_Ref is None:
        message = "Log in required to view this page"
        return redirect('Log In')
    else:
        vendor = Vendor.objects.get(referenceKey=vendor_Ref)
        vendor_Name = vendor.vendor_name
        welcome_message = vendor_Name
        vendor_items = Food_Item.objects.filter(vendorOwner=vendor)
        context = {'vendor_name':vendor_Name, 'welcome_message': welcome_message, 'vendor_items': vendor_items}
        return render(request, 'vendorpage/vendor.html', context)

def update_items_vendor_page(request):
    vendor_Ref = request.session.get('vendor_Ref')
    vendor = Vendor.objects.get(referenceKey=vendor_Ref)
    vendor_Name = vendor.vendor_name
    vendor_items = Food_Item.objects.filter(vendorOwner=vendor)
    print("Test:")
    check = request.POST.getlist('avail_box[]')
    deleted = request.POST.getlist('delete_box[]')
    print(vendor_items)
    print(check)
    for i in vendor_items:
        i.unavail()
        i.save()
        print(i.id)
        for avail_item in check:
            print('testing: ' + str(i.item_name))
            if (int(avail_item) == int(i.id)):
                print('Available: ' + str(i))
                i.avail()
                i.save()
                break

    for i in vendor_items:
        for avail_item in deleted:
            if (int(avail_item) == int(i.id)):
                print('deleted: ' + str(i))
                i.delete()
                break

    context = {'vendor_name':vendor_Name, 'vendor_items': vendor_items}
    return render(request, 'vendorpage/vendor.html', context)

def add_new_item(request):
    food_item_form = FoodItemForm(request.POST or None)
    vendor_Ref = request.session.get('vendor_Ref')
    vendorOwner = Vendor.objects.get(referenceKey=vendor_Ref)
    vendor_Name = vendorOwner.vendor_name
    if food_item_form.is_valid():
        item_name = food_item_form.cleaned_data.get("item_name")
        item_desc = food_item_form.cleaned_data.get("item_desc")
        item_cost = food_item_form.cleaned_data.get("item_cost")
        item_avail = food_item_form.cleaned_data.get("item_avail")
        food_item = Food_Item.objects.create(item_name=item_name, item_desc=item_desc, item_cost=item_cost, item_avail=True, vendorOwner=vendorOwner)
        food_item_form = FoodItemForm()
        return render(request, 'vendorpage/add_new_item.html', {"food_item_form": food_item_form, 'object': food_item, 'created': True, 'item_name': item_name, 'vendor_name': vendor_Name})

    return render(request, 'vendorpage/add_new_item.html', {"food_item_form": food_item_form, 'created': False, 'vendor_name': vendor_Name})



from .forms import VendorProfileForm
from django.shortcuts import render, redirect
from django.urls import reverse

def add_vendor_profile(request):
    vendor_Ref = request.session.get('vendor_Ref')
    vendorOwner = Vendor.objects.get(referenceKey=vendor_Ref)
    vendor_Name = vendorOwner.vendor_name

    try:
        vendor_profile = VendorProfile.objects.get(stall_name=vendorOwner)
    except VendorProfile.DoesNotExist:
        vendor_profile = None

    if request.method == 'POST':
        form = VendorProfileForm(request.POST, request.FILES, instance=vendor_profile)
        if form.is_valid():
            vendor_profile = form.save(commit=False)
            vendor_profile.stall_name = vendorOwner
            vendor_profile.save()
            return redirect(reverse('Vendor Page'))
            #return redirect("Vendor Page")
    else:
        form = VendorProfileForm(instance=vendor_profile)

    return render(request, 'vendorpage/add_vendor_profile.html', {'form': form, 'vendor_name': vendor_Name, 'vendor_image': vendor_profile.stall_image if vendor_profile else None})
