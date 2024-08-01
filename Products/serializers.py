from rest_framework import serializers 
from .models import Categorys,Products ,Reviews
from django.contrib.auth.models import User
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Categorys
        fields='__all__'
class ReviewSerializer(serializers.ModelSerializer):
    user=serializers.ReadOnlyField(source="user.username")
    category=serializers.ReadOnlyField(source="category.Name")
    product=serializers.ReadOnlyField(source="product.Name")
    class Meta:
        model=Reviews
        fields='__all__'


class ProductSerializer(serializers.ModelSerializer):
    reviews=serializers.SerializerMethodField(method_name="get_reviews",read_only=True)
    final_price=serializers.SerializerMethodField(method_name="get_final_price",read_only=True)

  
    user=serializers.ReadOnlyField(source="user.username")
    category=serializers.ReadOnlyField(source="category.Name")

   
    class Meta:
        model=Products
        fields="__all__"


   
    def get_final_price(self,obj):
        Finalprice=obj.Price - (obj.Price * (obj.DiscountPrice / 100))


        if(obj.DiscountPrice > 100 ):
            return None
       
        return  Finalprice 
      
      

    def get_reviews(self,obj):
        reviews=obj.reviews.all()
      
        serializer=ReviewSerializer(reviews,many=True)
        return serializer.data







       
