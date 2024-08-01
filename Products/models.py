from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# --------------------------------------------Create your models here-------------------------------------#.
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
class Categorys(models.Model):
    Name=models.CharField(max_length=255)
    create=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.Name
    
class Products(models.Model):
    category=models.ForeignKey(Categorys,on_delete=models.CASCADE)

    user=models.ForeignKey(User,on_delete=models.CASCADE)

    Name=models.CharField(max_length=255)

    Description=models.TextField()

    Price=models.DecimalField( max_digits=5, decimal_places=2,default=0.00)

    DiscountPrice=models.DecimalField( max_digits=5, decimal_places=2,default=0.00)

    Stock=models.PositiveIntegerField()

    photo=models.ImageField(upload_to='Product/',blank=True,null=True)

    color=models.CharField(max_length=255,choices=Color)

    size=models.CharField(max_length=255,choices=Size)

    ratings=models.DecimalField(max_digits=3,decimal_places=2,default=0.00)

    slug=models.SlugField(blank=True,null=True)

    create=models.DateTimeField(auto_now_add=True)

    update=models.DateTimeField(auto_now=True)

    def save(self,*args,**kwargs):
      
        self.slug=slugify(self.Name)
       
        return super(Products,self).save(*args,**kwargs)
    
   
    

    def __str__(self) -> str:
        return self.Name


class Reviews(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE,related_name="reviews")
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    reting=models.PositiveIntegerField()
    comment=models.TextField()
    create=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)


    




    def __str__(self) -> str:
        return self.product.Name

    
