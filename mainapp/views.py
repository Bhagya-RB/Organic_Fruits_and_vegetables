from django.shortcuts import render
from adminapp.models import ProductModel
from mainapp.models import ContactModel

# Create your views here.
def home(request):
    return render(request,"main/index.html")

def about(request):
    return render(request,"main/about.html")

def products(request):
    ProductModeldisplay =ProductModel.objects.all()
    return render(request,"main/products.html",{"ProductModel":ProductModeldisplay})

# def vegetables(request):
#     return render(request,"main/vegetables.html")

# def millets(request):
#     return render(request,"main/millets.html")

# def dried(request):
#     return render(request,"main/dried.html")

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        ContactModel.objects.create(name=name, email=email, subject=subject, message=message)

    return render(request,"main/contact.html")

def cart(request):
    return render(request,"main/cart.html")