from django.shortcuts import get_object_or_404
from .serializers import  ShoppineAddressSerializers
from rest_framework import status
from  rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import ShoppineAddress
from Order.models import Order
# Create your views here.
class CheckoutAddress():
    #-------------------createAddress---------------------------------#
    @api_view(["POST"])
    @permission_classes([IsAuthenticated])
    def createAddress(request):
        data=request.data
        user=request.user

        order=get_object_or_404(Order, user=user,is_finished=False)
        address=ShoppineAddress.objects.filter(orders=order,user=request.user)

        if  check.exists():
            new_address={
                "firstAddress":data["firstAddress"],
                "secondAddress":data["secondAddress"],
                "mobilePhone":data["mobilePhone"],
                "Country":data["Country"],
                "City":data["City"],
                "State":data["State"],
                "zipCode":data["zipCode"],
                "Payment":data["Payment"],

            }
            address.update(**new_address)
            return Response({"massages":"your  Address is update"},status=status.HTTP_202_ACCEPTED)
        else:
       
            shoppine_address =ShoppineAddress.objects.create(
                user=user,
                orders=order,
                firstAddress=data["firstAddress"],
                secondAddress=data["secondAddress"],
                mobilePhone=data["mobilePhone"],
                Country=data["Country"],
                City=data["City"],
                State=data["State"],
                zipCode=data["zipCode"],
                Payment=data["Payment"],
            )
        shoppine_address .save()
        return Response({"massages":"your  Address is create"},status=status.HTTP_201_CREATED)
    #-------------------ShowAddress---------------------------------#
    