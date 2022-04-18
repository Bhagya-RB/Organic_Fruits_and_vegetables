from email.policy import default
from statistics import mode
from tkinter import CASCADE
import uuid
from django.db import models
from django import forms

from adminapp.models import ProductModel

# Create your models here.
class ConsumerModel(models.Model):
    consumer_id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    mobile=models.BigIntegerField(null=True)
    email = models.EmailField(max_length=1000)
    profile=models.ImageField(default=False)
    address=models.TextField(max_length=100, default=False)
    password = models.CharField(max_length=2000)
    status=models.CharField(max_length=500,default="pending")
    reg_date = models.DateField(auto_now_add=True, null=True)


    class Meta:
        db_table = 'Consumer_Details'

      
# Create consumer Feedback model
class ConsumerFeedbackModel(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20, null=True)
    last_name=models.CharField(max_length=50, null=True)
    email=models.EmailField(max_length=45, null=True)
    message=models.TextField(max_length=1000)
    feedback_date = models.DateField(auto_now_add=True, null=True)

    class Meta:
       db_table = 'Consumer_Feedback_Details'


#Create Add tocart model here.
class CartModel(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(ConsumerModel,on_delete=models.CASCADE, null=True)
    completed = models.BooleanField(default=False)
        
    class Meta:
        db_table = 'user_cart'

class CartItemsModel(models.Model):
    user = models.IntegerField(null=True)
    cart = models.ForeignKey(CartModel, on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    
    class Meta:
        db_table = 'user_cart_items'

class OrderModel(models.Model):
    order_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    cart_id = models.IntegerField()
    order_status = models.CharField(max_length=50, default='pending')
    payment_mode = models.CharField(max_length=100, default='pending')
    order_date= models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'order_items'

