from .views import CheckoutAddress
from django.urls import path



urlpatterns = [
    path("create/",CheckoutAddress.createAddress),
    
   

]


