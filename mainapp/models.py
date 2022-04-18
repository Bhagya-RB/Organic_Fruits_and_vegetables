from django.db import models

# Create your models here.
class ContactModel(models.Model):
    contact_id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=55)
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=2000)
    reg_date = models.DateField(auto_now_add=True, null=True)

    
    class Meta:
        db_table = 'contact_details'

    
