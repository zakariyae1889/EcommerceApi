from django.db import models
from django.contrib.auth.models import User
from Products.models import Products


class Color(models.TextChoices):
    Read="Read"
    Green="Green"
    Black="Black"
    White="White"
    Blue="Blue"
class Size(models.TextChoices):
    s="s"
    xs="xs"
    m="m"
    l="l"
    xl="xl"
    xxl="xxl"




class Order(models.Model):
      
    user=models.ForeignKey(User,on_delete=models.CASCADE)
   
    
    is_finished=models.BooleanField(default=False)
    


    orderCreate=models.DateTimeField(auto_now_add=True)
    orderUpdate=models.DateTimeField(auto_now=True)
   
   
    
    
   
    

   

    def __str__(self):
        return str( self.pk)

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

class OrderDetails(models.Model):
    product=models.ForeignKey(Products,null=True,on_delete=models.SET_NULL)

    order=models.ForeignKey(Order,null=True,on_delete=models.CASCADE,related_name="order_details")

    color=models.CharField(max_length=255,choices=Color)

    size=models.CharField(max_length=255,choices=Size)

    quantity=models.PositiveIntegerField(default=1)

    
    
   

   

    


  


    

   
    
   
   
    def __str__(self) -> str:

        return self.product.Name
