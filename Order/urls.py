from django.urls import path
from .views import Orders

urlpatterns = [
    
    path("",Orders.showOrderDetials),
    path("<slug:slug>/",Orders.createOrder),
    path("<int:pk>/update",Orders.UpdateOrder),
    path("<int:pk>/delete",Orders.RemoveOrder),
]

