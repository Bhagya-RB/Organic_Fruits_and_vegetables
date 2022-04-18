from django.db import models

# Create your models here.
class SupplierModel(models.Model):
    supplier_id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    mobile=models.BigIntegerField(null=True)
    email =models.EmailField(max_length=50)
    profile=models.ImageField(default=False)
    address=models.TextField(max_length=100, default=False)
    password = models.CharField(max_length=55)
    status=models.CharField(max_length=500,default="pending")
    reg_date = models.DateField(auto_now_add=True, null=True)

    class Meta:
        db_table = 'Supplier_Details'



# Supplier verify models here.
class SupplierVerifyModel(models.Model):
    supplierverify_id = models.AutoField(primary_key=True)
    distributor_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phonenumber = models.BigIntegerField(null=True)
    address= models.TextField(max_length=250)
    country=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    pincode=models.BigIntegerField()
    isimark=models.CharField(max_length=50)
    logo=models.ImageField(upload_to="",default="")
    status=models.CharField(max_length=500,default="pending")
    verify_date = models.DateField(auto_now_add=True, null=True)


    class Meta:
        db_table = 'Supplier_Verified_Details'
  


