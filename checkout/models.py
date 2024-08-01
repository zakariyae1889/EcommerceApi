from django.db import models
from django.contrib.auth.models import  User
from Order.models import Order
# Create your models here.
class TypePayment(models.TextChoices):
    Paypal="Paypal"
    DirectCheck="DirectCheck"
    BankTransfer="BankTransfer"
class ShoppineAddress(models.Model):
    
   user=models.ForeignKey(User,on_delete=models.CASCADE)
   orders=models.ForeignKey(Order,on_delete=models.CASCADE)
   firstAddress=models.CharField(max_length=255)
   secondAddress=models.CharField(max_length=255,blank=True,null=True)
   mobilePhone=models.CharField(max_length=255)
   Country=models.CharField(max_length=255)
   City=models.CharField(max_length=255)
   State=models.CharField(max_length=255)
   zipCode=models.PositiveIntegerField()
   Payment=models.CharField(max_length=255,choices=TypePayment)
   def __str__(self):
        return self.user.username

   def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
