from .views import product
from django.urls import path



urlpatterns = [
    path("",product.allProduct),
    path("<slug:slug>/",product.productDetails),
    path("reviews/<slug:slug>/",product.createReview),
    path("trandproduct",product.Trandyproducts),
    path("lastproduct",product.Lastproduct),
    path("category/<str:Name>",product.getProduct_by_category),
   

]


