from ast import Add
from cgi import print_exception
from math import prod
from django.contrib import messages
from unicodedata import name
from django.shortcuts import get_object_or_404, redirect, render
from adminapp.models import *
from consumerapp.models import CartModel, ConsumerFeedbackModel, ConsumerModel,OrderModel
from supplierapp.models import *
from django.db.models import Max
from mainapp.models import *

# Create your views here.

def admin_home(request):
    suppliers_count =SupplierModel.objects.count()
    consumers_count =ConsumerModel.objects.count()
    consumers_feedback = ConsumerFeedbackModel.objects.count()
    products_details=ProductModel.objects.count()
    verify_supplier=SupplierVerifyModel.objects.count()
    return render(request,"admin/admin-dashboard.html",{"suppliers_count":suppliers_count,"consumers_count":consumers_count,"consumers_feedback":consumers_feedback,"products_details":products_details,"verify_supplier":verify_supplier})

def admin_view_enquiry(request):
    ContactModeldisplay=ContactModel.objects.all()
    return render(request,"admin/admin-viewenquiry.html",{"ContactModel":ContactModeldisplay})


#Admin login page
def admin_login(request):
    if request.method == "POST":
        name = request.POST.get('email')
        password = request.POST.get('password')
        if name == 'admin' and password == 'admin' :
            messages.success(request, "login successfully")
            return redirect('admin-home')
        else:
            messages.error(request,"invalid login")
    return render(request,"admin/admin-login.html")

#Admin view profile
def admin_view_profile(request):
    return render(request,"admin/admin-viewprofile.html")

#Admin Add fruit views
def admin_add_products(request):
    ProductModeldisplay = ProductModel.objects.all()
    # prod_id = ProductModel.objects.all().aggregate(Max("prod_id"))["prod_id__max"] + 1
    if request.method == "POST" and request.FILES["prod_image"]:
        prod_id = request.POST['prod_id']
        prod_category = request.POST['prod_category']
        prod_name= request.POST['prod_name']
        # prod_id = 'F' + str(prod_id) 
        prod_price = request.POST['prod_price']
        prod_units = request.POST['prod_units']
        prod_description = request.POST['prod_description']
        prod_image = request.FILES['prod_image']
        ProductModel.objects.create(prod_id=prod_id, prod_category=prod_category, prod_name=prod_name, prod_price=prod_price, prod_units=prod_units, prod_description=prod_description, prod_image=prod_image)
    return render(request,"admin/admin-addproducts.html",{"ProductModel":ProductModeldisplay})


def admin_view_consumer(request):
    ConsumerModeldisplay =ConsumerModel.objects.all()
    return render(request,"admin/admin-viewconsumer.html",{"ConsumerModel":ConsumerModeldisplay})

def accept_consumer(request,id):
    accept = get_object_or_404(ConsumerModel,consumer_id=id)
    accept.status ="Accepted"
    accept.save(update_fields=['status'])
    accept.save()
    return redirect('admin-viewconsumer')

def reject_consumer(request,id):
    reject=get_object_or_404(ConsumerModel,consumer_id=id)
    reject.status="Rejected"
    reject.save(update_fields=['status'])
    reject.save()
    return redirect('admin-viewconsumer')

#Views for Supplier Verify model


def admin_verify_supplier(request):
    SupplierVerifyModeldisplay = SupplierVerifyModel.objects.all()
    return render(request,"admin/admin-verifysupplier.html",{"SupplierVerifyModel":SupplierVerifyModeldisplay})

def accept_verify_supplier(request,id):
    accept = get_object_or_404(SupplierVerifyModel,supplierverify_id=id)
    accept.status ="Accepted"
    accept.save(update_fields=['status'])
    accept.save()
    return redirect('admin-verifysupplier')

def reject_verify_supplier(request,id):
    reject=get_object_or_404(SupplierVerifyModel, supplierverify_id=id)
    reject.status="Rejected"
    reject.save(update_fields=['status'])
    reject.save()
    return redirect('admin-verifysupplier')

#Views for Supplier Registration model

def admin_view_supplier(request):
    SupplierModeldisplay = SupplierModel.objects.all()
    return render(request,"admin/admin-viewsupplier.html",{"SupplierModel":SupplierModeldisplay})

def accept_supplier(request,id):
    accept = get_object_or_404(SupplierModel,supplier_id=id)
    accept.status ="Accepted"
    accept.save(update_fields=['status'])
    accept.save()
    return redirect('admin-viewsupplier')

def reject_supplier(request,id):
    reject=get_object_or_404(SupplierModel, supplier_id=id)
    reject.status="Rejected"
    reject.save(update_fields=['status'])
    reject.save()
    return redirect('admin-viewsupplier')


def admin_view_orders(request):
    OrderModeldisplay = OrderModel.objects.all()
    # consumer_id=request.session["consumer_id"]
    # consumer = ConsumerModel.objects.filter(consumer_id=consumer_id)
    # cart = CartModel.objects.filter(cart_id=id)
    # if request.
    # ,{"OrderModel":OrderModeldisplay}
    return render(request,"admin/admin-vieworders.html",{"OrderModel":OrderModeldisplay})

def admin_view_added_products(request):
    ProductModeldisplay = ProductModel.objects.all()
    return render(request,"admin/admin-viewalladdedproducts.html", {"ProductModel":ProductModeldisplay})

def admin_edit_added_products(request,id):
    edit = ProductModel.objects.filter(prod_id=id)
    obj = get_object_or_404(ProductModel,prod_id=id)
    if request.method =='POST':
        prod_category = request.POST.get('prod_category')
        prod_name = request.POST.get('prod_name')
        prod_price = request.POST.get('prod_price')
        prod_units = request.POST.get('prod_units')
        

        obj.prod_name = prod_name
        obj.prod_category = prod_category
        obj.prod_price = prod_price
        obj.prod_units = prod_units
      
        obj.save(update_fields=['prod_category','prod_name', 'prod_price','prod_units'])
        obj.save()
        if obj.save():
            messages.success(request,"Product Updates Successfully...")
        else:
            messages.error(request,"something went wrong!")
    return render(request,"admin/admin-editaddedproducts.html",{'edit':edit})

def admin_view_payment(request):
    return render(request,"admin/admin-viewpayment.html")

def delete_products(request,id):
    d=ProductModel.objects.filter(prod_id=id)
    d.delete()
    return redirect("admin-viewalladdedproducts")

def admin_view_feedback(request):
    ConsumerFeedbackModeldisplay = ConsumerFeedbackModel.objects.all()
    return render(request,"admin/admin-viewfeedback.html",{"ConsumerFeedbackModel":ConsumerFeedbackModeldisplay})
