from pyexpat.errors import messages
from django.contrib import messages
from urllib.request import Request
from django.shortcuts import get_object_or_404, render, redirect
from consumerapp.models import CartModel, CartItemsModel, ConsumerFeedbackModel, ConsumerModel, OrderModel
from adminapp.models import ProductModel

# Create your views here.


def consumer_home(request):
    products_details=CartModel.objects.count()
    return render(request,"consumer/consumer-dashboard.html",{"products_details":products_details})

def consumer_view_products(request):
     ProductModeldisplay = ProductModel.objects.all()
     return render(request,"consumer/consumer-viewproducts.html",{"ProductModel":ProductModeldisplay})

# def consumer_products(request):
#      ProductModeldisplay = ProductModel.objects.all()
#      return render(request,"consumer/consumer-products.html",{"ProductModel":ProductModeldisplay})

# def consumer_vegetables(request):
#     ProductModeldisplay = ProductModel.objects.all()
#     return render(request,"consumer/consumer-vegetables.html",{"ProductModel":ProductModeldisplay})

# def consumer_millets(request):
#     ProductModeldisplay = ProductModel.objects.all()
#     return render(request,"consumer/consumer-millets.html",{"ProductModel":ProductModeldisplay})

# def consumer_dried(request):
#     ProductModeldisplay = ProductModel.objects.all()
#     return render(request,"consumer/consumer-dried.html",{"ProductModel":ProductModeldisplay})

def consumer_reg(request):
    if request.method == "POST" and request.FILES["profile"]:
        name = request.POST['name']
        mobile =request.POST['mobile']
        email = request.POST['email']
        password = request.POST['password']
        profile= request.FILES["profile"]
        address=request.POST['address']
        ConsumerModel.objects.create(name=name,mobile=mobile, email=email, password=password,profile=profile,address=address)  
    return render(request,"consumer/consumer-registration.html")

def consumer_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            check = ConsumerModel.objects.get(email=email, password=password,status="Accepted")
            request.session["consumer_id"]=check.consumer_id
            messages.success(request,"Loggged in successfully")
            return redirect("consumer-home")
        except:
            messages.error(request,"Invalid Login")
    return render(request,"consumer/consumer-login.html")

def consumer_view_profile(request):
    consumer_id =request.session["consumer_id"]
    profile = ConsumerModel.objects.filter(consumer_id=consumer_id) 
    obj=get_object_or_404(ConsumerModel,consumer_id=consumer_id)
    if request.method == 'POST':
        name= request.POST.get('name')
        email=request.POST.get('email')
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        if len(request.FILES) != 0:
            profile_image = request.FILES['profile']
            obj.name =name
            obj.email=email
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
    return render(request,"consumer/consumer-viewprofile.html",{'profile':profile})
          

# def consumer_detail_of_products(request,id):
#     # cart=CartModel.objects.all()
#     consumer_id = request.session["consumer_id"]
#     user = ConsumerModel.objects.get(consumer_id=consumer_id)
#     # print(user.consumer_id)
#     product = ProductModel.objects.get(prod_id=id)
#     product1 = ProductModel.objects.filter(prod_id=id)
#     print(product1)
#     price=ProductModel.objects.get(prod_id=id)
#     # print(product.prod_id)
#     # print(product.prod_price)
#     if request.method == "POST":
#         qty=request.POST.get('qty')
#         pid=request.POST.get('prod_id')

#         print(consumer_id)
#         print(qty)
#         print(pid)
#         CartModel.objects.create(user=user)


#         return redirect('consumer-CartModel')  
#     return render(request,"consumer/consumer-detailofproduct.html",{"ProductModel":product1})

def consumer_detail_of_products(request,id):
    consumer_id=request.session["consumer_id"]
    user = ConsumerModel.objects.filter(consumer_id=consumer_id).first()
    print(user.consumer_id)
    # count = CartModel.objects.count()
    prod = ProductModel.objects.filter(prod_id=id)
    # price = AdminModel.objects.filter(prod_id=id).values_list('prod_price')
    # cart_count = CartModel.objects.filter(user_id=user_id).all().exclude(status='paid').count()
    cart = CartModel.objects.filter(user=consumer_id).first()
    # print(cart.query)
    # print(cart.cart_id)
    prod = ProductModel.objects.get(prod_id=id)
    prod1 = ProductModel.objects.filter(prod_id=id)
    price = prod1.values_list("prod_price")[0][0]

    if request.method=="POST":
        qty=request.POST.get("qty")
        qty1 = int(qty)

       
        # pid=request.POST.get("prod_id")
      
        # CartModel.objects.create(user=UserModel.objects.get(user_id=user_id),prod=AdminModel.objects.get(prod_id=pid),quantity=qty,price=price).save()

        CartModel.objects.create(user=user)
        cart = CartModel.objects.filter(user=consumer_id).first()
        CartItemsModel.objects.create(user=consumer_id,cart=cart,product=prod,quantity=qty1,price=price)
        return redirect("consumer-CartModel")
    
    # return render(request,'main/user-product-details.html',{'products_det':prod,'data':user,'qty':count,'c_c':cart_count})

    return render(request,"consumer/consumer-detailofproduct.html",{"ProductModel":prod1})


# def consumer_add_to_cart(request):
#     count =CartModel.objects.count()
#     consumer_id=request.session["consumer_id"]
#     data = ConsumerModel.objects.get(consumer_id=consumer_id)
    
#     # qty = CartDetailsModel.objects.count()
#     # if CartDetailsModel.objects.filter(status="pending"):
#     #     prod= CartDetailsModel.objects.all()
#     # else:
#     prod = CartModel.objects.all()
#     # cart_count = CartDetailsModel.objects.all().exclude(status='paid').count()
#     # cartid = CartModel.objects.filter(user=consumer_id).values_list("cart_id")
#     # price = CartModel.objects.filter(user=consumer_id).values_list("price")
#     # # products_count = CartDetailsModel.objects.all().exclude(status='paid').aggregate(prod_total=Sum("quantity"),total_price=Sum("price"))
    
#     # print(products_count)
#     if request.method == "POST":
#         print("something...")
#         address = request.POST.get("address")
#         cid = request.POST.get("cart_id")
#         print(address)
#         cart_id=int(cid)
#         # OrderModel.objects.create(consumer_id=ConsumerModel.objects.get(consumer_id=consumer_id),cart_id=CartModel.objects.get(cart_id=cart_id),address=address,price=price)
        
#         # record = CartDetailsModel.objects.filter(user_id=user_id).update(status='paid')
#         # record.status='booked'
#         # record.save(update_fields=['status'])
#         return redirect("consumer-checkout")
#     return render(request,"consumer/consumer-addtocart.html",{"data":data})


def consumer_add_to_cart(request):
    consumer_id=request.session["consumer_id"]
    
    cart_id = CartModel.objects.filter(user=consumer_id,completed=False).values_list("cart_id")[0][0]


    cart = CartItemsModel.objects.filter(user=consumer_id,cart_id=cart_id)

    if request.method=="POST":
        OrderModel.objects.create(user_id=consumer_id, cart_id=cart_id)
        CartModel.objects.filter(user=consumer_id,completed=False).update(completed=True)
    

    return render(request,"consumer/consumer-addtocart.html",{"cart":cart})


def consumer_orders(request):
    consumer_id=request.session["consumer_id"]
    data=ConsumerModel.objects.filter(consumer_id=consumer_id)
    cartdetails=ProductModel.objects.count()
    # order=OrderModel.objects.all()

    return render(request,"consumer/consumer-addtocart.html",{"cart_details":cartdetails})


def consumer_add_to_wishlist(request):
    return render(request,"consumer/consumer-addtowishlist.html")

def consumer_checkout(request):
    return render(request,"consumer/consumer-checkout.html")

def consumer_credit_card_payment(request):
    return render(request,"consumer/consumer-creditcardpayment.html")

def consumer_debit_card_payment(request):
    return render(request, "consumer/consumer-debitcardpayment.html")

def conusmer_net_banking(request):
    return render(request,"conusmer/consumer-netbanking.html")

def consumer_feedback(request):
    if request.method == "POST":
        first_name = request.POST['name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        message = request.POST['message']
        ConsumerFeedbackModel.objects.create(first_name=first_name, last_name=last_name,email=email, message=message)
    return render(request,"consumer/consumer-feedback.html")

def fpass(request):

    return render(request,'consumer-forgotpassword.html')
    



