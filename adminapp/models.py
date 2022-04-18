from distutils.command.upload import upload
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models


# Create your models here.

class ProductModel(models.Model):
    p_id=models.AutoField(primary_key=True)
    prod_id =models.CharField(max_length=10)
    prod_category=models.CharField(max_length=10,default=False)
    prod_name=models.CharField(max_length=50)
    prod_price=models.IntegerField()
    prod_units=models.CharField(max_length=20, default=False)
    prod_description=models.TextField(max_length=500)
    prod_image=models.ImageField(upload_to="images/")
    prod_status=models.CharField(default='available',max_length=50)
    prod_date=models.DateField(auto_now_add=True)

    class Meta:
       db_table = 'product_details'



