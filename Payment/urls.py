from .views import Payments
from django.urls import path


urlpatterns = [
    path("create/",Payments.createPayment)
]
