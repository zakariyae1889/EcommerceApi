from django.shortcuts import get_object_or_404
from .serializers import PaymentSerializer
from .models import Payment
from rest_framework.decorators import permission_classes,api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from Order.models import Order

class Payments():
    @api_view(["POST"])
    @permission_classes([IsAuthenticated])
    def createPayment(request):
        data=request.data
        user=request.user
        orders=Order.objects.filter(user=user,is_finished=False)
        if orders:
            order=get_object_or_404(Order,user=user,is_finished=False)
            payments=Payment.objects.create(
                user=user,
                orders=order,
                cc_number=data["cc_number"],
                cc_expiry=data["cc_expiry"],
                cc_code=data["cc_code"]
            )
            payments.save()
            order.is_finished=True
            order.save()
        return Response({"message":"Your order is finished"},status=status.HTTP_202_ACCEPTED)


