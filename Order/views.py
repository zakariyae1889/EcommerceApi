from django.shortcuts import get_object_or_404,HttpResponse
from .serializer import OrderDetailsSerializer,OrderSerializer
from .models import Order,OrderDetails,Products
from rest_framework.decorators import permission_classes,api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializer import OrderDetailsSerializer
class Orders():
    #--------------Create-------------------------#
    @api_view(["POST"])
    @permission_classes([IsAuthenticated])
    def createOrder(request,slug):
        try:
            product=get_object_or_404(Products,slug=slug)
            data=request.data
            user=request.user
           

            order=Order.objects.filter(user=user,is_finished=False)
            if order:
                old_order=get_object_or_404(Order, user=user,is_finished=False)
                order_details=OrderDetails.objects.filter(order=old_order,product=product)
               
                if order_details.exists():
                    
                 


                    new_order_details={
                        "quantity":data["quantity"],
                        "size":data["size"],
                        "color":data["color"],
                        
                     
                    }
                    order_details.update(**new_order_details)
                    if (product.Stock==0 or product.Stock <  new_order_details.get('quantity') ):
                         return Response({"massages":"error in your  order  or stock is empty"},status=status.HTTP_400_BAD_REQUEST)
                    else:
                        product.Stock-=new_order_details.get('quantity')
                        product.save()
                    return Response({"massages":" order  update"},status=status.HTTP_200_OK)
                else:
                    orderItem=OrderDetails.objects.create(
                        product=product,
                        order=old_order,
                        quantity=data["quantity"],
                        size=data["size"],
                        color=data["color"],
                       

                    )
                    orderItem.save()
                    if (product.Stock==0 or product.Stock < orderItem.quantity ):
                         return Response({"massages":"error in your order  or stock is empty"},status=status.HTTP_400_BAD_REQUEST)
                    else:
                        product.Stock-=orderItem.quantity
                        product.save()
                    return Response({"massages":" order  create "},status=status.HTTP_201_CREATED)
            else:
                
                new_order=Order()
                new_order.user=request.user
                new_order.is_finished=False

                new_order.save()
                
                orderItem=OrderDetails.objects.create(
                    product= product,
                    order=new_order,
                    quantity=data["quantity"],
                    size=data["size"],
                    color=data["color"],
                   
                   
                )
                orderItem.save()
                if (product.Stock==0 or product.Stock <  orderItem.quantity):
                        return Response({"massages":"error in  your order or stock is empty"},status=status.HTTP_400_BAD_REQUEST)
                else:
                    product.Stock-=orderItem.quantity
                    product.save()
               
            return Response({"massages":" order create"},status=status.HTTP_201_CREATED)
        except Order.DoesNotExist:
            return Response({"message":"error"},status=status.HTTP_404_NOT_FOUND)
    #--------------Display-------------------------#
    @api_view(["GET"])
    @permission_classes([IsAuthenticated])
    def showOrderDetials(request):
        try:
            user=request.user
            orders=Order.objects.filter(user=user)
            serializer=OrderSerializer(orders,many=True)
            return Response({"Order":serializer.data})
        except Order.DoesNotExist:
            return Response({"message":"error"},status=status.HTTP_404_NOT_FOUND)
    #--------------------Update-------------------#
    @api_view(["PUT"])
    @permission_classes([IsAuthenticated])
    def UpdateOrder(request,pk):
        try:
            order=get_object_or_404(Order,pk=pk)
            orders=get_object_or_404(OrderDetails,order=order)
          
            orders.quantity=request.data["quantity"]
            orders.size=request.data["size"],
            orders.color=request.data["color"],
            orders.save()
            seiralizer=OrderDetailsSerializer(orders,many=False)
            return Response({"order":seiralizer.data})
        except Order.DoesNotExist:
            return Response({"message":"error"},status=status.HTTP_404_NOT_FOUND)
    #--------------------Delete--------------------#
    @api_view(["DELETE"])
    @permission_classes([IsAuthenticated])
    def RemoveOrder(request,pk):

        try:
            order=get_object_or_404(Order,pk=pk)
            order.delete()
            return Response({"massages":" order is delete"},status=status.HTTP_200_OK)
        except Order.DoesNotExist:
            return Response({"message":"error"},status=status.HTTP_404_NOT_FOUND)
    #----------------------------------------#