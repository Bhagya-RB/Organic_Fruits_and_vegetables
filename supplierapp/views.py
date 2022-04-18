from pyexpat.errors import messages
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from consumerapp.models import CartItemsModel,CartModel,ConsumerFeedbackModel,ConsumerModel
from supplierapp.models import SupplierModel
from supplierapp.models import SupplierVerifyModel
from adminapp.models import ProductModel

# Create your views here.
def supplier_home(request):
    consumers_count =ConsumerModel.objects.count()
    consumers_feedback = ConsumerFeedbackModel.objects.count()
    products_details= ProductModel.objects.count()
    return render(request,"supplier/supplier-dashboard.html",{"consumers_count":consumers_count,"consumers_feedback":consumers_feedback,"products_details":products_details})

def supplier_reg(request):
    if request.method == "POST" and request.FILES["profile"]:
        name = request.POST['name']
        mobile =request.POST['mobile']
        email = request.POST['email']
        password = request.POST['password']
        profile= request.FILES['profile']
        address=request.POST['address']
        SupplierModel.objects.create(name=name, mobile=mobile, email=email, password=password,profile=profile, address=address)

    return render(request,"supplier/supplier-registration.html")

def supplier_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            check = SupplierModel.objects.get(email=email, password=password,status="Accepted")
            request.session["supplier_id"]=check.supplier_id
            messages.success(request,"Valid Login")
            return redirect("supplier-home")
        except:
            messages.error(request,"Valid Login")
            
    return render(request,"supplier/supplier-login.html")

def supplier_view_profile(request):
    supplier_id =request.session["supplier_id"]
    profile = SupplierModel.objects.filter(supplier_id=supplier_id) 
    obj=get_object_or_404(SupplierModel,supplier_id=supplier_id)
    if request.method == "POST":
        name= request.POST['name']
        email=request.POST.get('email')
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        if len(request.FILES) != 0:
            profile_image = request.FILES['profile']
            obj.name = name
            obj.email = email
            obj.address = address
            obj.mobile = mobile
            obj.profile = profile_image
            obj.save(update_fields=['name','profile','email','address','mobile'])
        else:
            obj.name =name
            obj.email=email
            obj.address=address
            obj.mobile=mobile
            obj.save(update_fields=['name','email','address','mobile'])
    return render(request,"supplier/supplier-viewprofile.html",{'profile':profile})

def supplier_view_orders(request):
    # OrderModeldisplay = OrderModel.objects.create()
    return render(request,"supplier/supplier-vieworders.html")

def supplier_order_history(request):
    return render(request,"supplier/supplier-orderhistory.html")

def supplier_verify_supplier(request):
    if request.method == "POST" and request.FILES['logo']:
        distributor_name = request.POST['name']
        company_name = request.POST['cname']
        email = request.POST['email']
        phonenumber =request.POST['phonenumber']
        address=request.POST['address']
        country=request.POST['country']
        state=request.POST['state']
        pincode=request.POST['pincode']
        isimark=request.POST['isimark']
        logo=request.FILES['logo']
        SupplierVerifyModel.objects.create(distributor_name=distributor_name,company_name=company_name,email=email,phonenumber=phonenumber,address=address,country=country,state=state,pincode=pincode,isimark=isimark,logo=logo)
    return render(request,"supplier/supplier-verifysupplieraccount.html")

def supplier_view_feedback(request):
    ConsumerFeedbackModeldisplay = ConsumerFeedbackModel.objects.all()
    return render(request,"supplier/supplier-viewfeedback.html",{"ConsumerFeedbackModel":ConsumerFeedbackModeldisplay})
