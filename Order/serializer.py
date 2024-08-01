from rest_framework import serializers
from .models import Order,OrderDetails,Products
from Products.serializers import ProductSerializer
class OrderDetailsSerializer(serializers.ModelSerializer):

    product=ProductSerializer()

    sub_total=serializers.SerializerMethodField(method_name="get_sub_total",read_only=True)
    


    class Meta:
        model=OrderDetails
        fields=[
            "color",
            "size",
            "product",
            "quantity",
            "sub_total",
          
        ]
    

    def get_sub_total(self,obj):
        Finalprice=( obj.product.Price-(obj.product.Price * (obj.product.DiscountPrice / 100)) )
        Quantity=obj.quantity
        sub_total=( Finalprice * Quantity)
        if(obj.product.DiscountPrice > 100 or obj.product.DiscountPrice < -1):
            return None
       
        return  sub_total

class OrderSerializer(serializers.ModelSerializer):
    order_details=OrderDetailsSerializer(many=True,read_only=True)

    user=serializers.ReadOnlyField(source="user.username")
    total_amount=serializers.SerializerMethodField(method_name="get_total_amount",read_only=True)
    
   

    class Meta:
        model=Order
        fields=[
            "id",
            "user",
            "order_details",
            "total_amount",
            
        ]
    def get_total_amount(self,obj):
        if(obj.order_details.product.DiscountPrice > 100 or obj.product.DiscountPrice < -1 ):
            return None
        total=sum(
            details.quantity 
            * 
            ( details.product.Price-(details.product.Price * (details.product.DiscountPrice / 100)) )  
            for details in obj.order_details.all()
        )
       
        return total
   
    
             
   

   

   