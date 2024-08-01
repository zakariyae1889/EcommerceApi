from django.shortcuts import get_object_or_404
from .serializers import CategorySerializer,ProductSerializer
from .models import Categorys,Products,Reviews
from .filter import  ProductFilter
from rest_framework import status
from  rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from django.db.models import Avg ,Q
#-------------------------------ClassProduct----------------------------------#
class product():
    #-------------------------ALLProduct---------------------------------#
    @api_view(['GET'])
    def allProduct(request):
        try:
            #query
            prod=Products.objects.all().order_by("-create")
            #fiter
            filterprod=ProductFilter(request.GET,queryset=prod)
            #pagination
            respage=4
            paginator=PageNumberPagination()
            paginator.page_size=1
            prodPagination=paginator.paginate_queryset(filterprod.qs,request)
            #serializer
            serializer=ProductSerializer(prodPagination,many=True)
        except Products.DoesNotExist:
            return Response({"massage":"bad Request"},status=status.HTTP_404_NOT_FOUND)
        return Response({
            "product":serializer.data
        })
    #---------------Detailsproduct-------------------#
    @api_view(['GET'])
    def productDetails(request,slug):
        try:
            #query
            prod=get_object_or_404(Products,slug=slug)
            #serializerprod
            serializerprod=ProductSerializer(prod,many=False)
        except Products.DoesNotExist:
            return Response({"massage":"bad Request"},status=status.HTTP_404_NOT_FOUND)
        return Response({"product":serializerprod.data})
    #-------------------------Trandproduct-------------------------------#
    @api_view(["GET"])
    def Trandyproducts(request):
        try:
            #query
            prod =  Products.objects.filter(Q(ratings__gte=4))
            #serializer
            serializer=ProductSerializer(prod,many=True)
        except Products.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response({
            "product":serializer.data,
        })
    #-----------------------Lastproduct-------------------------------#
    @api_view(["GET"])
    def Lastproduct(request):
        try:
            prod=Products.objects.all().order_by("-create")[0:8]
            serializer=ProductSerializer(prod,many=True)
        except Products.DoesNotExist:
            return Response({"massage":"bad Request"},status=status.HTTP_404_NOT_FOUND)
        return Response({
            "product":serializer.data
        })
    #----------------PostReview------------------#
    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def createReview(request,slug):
        prod=get_object_or_404(Products,slug=slug)
        data=request.data
        user=request.user
        review=prod.reviews.filter(user=user)
        if (data["reting"] <= 0  or data["reting"] > 5):
            return Response({"messageerror":"Please select between 1 to 5 only" },status=status.HTTP_400_BAD_REQUEST)
        elif review.exists():
            new_review={"reting":data["reting"] ,"comment":data['comment']}
            review.update(**new_review)
            rating=prod.reviews.aggregate(avg_ratings=Avg('reting'))
            prod.ratings=rating['avg_ratings']
            prod.save()
            return Response({"massages":"Product review update"})
        else:
            Reviews.objects.create(
                product=prod,
                user=user,
                reting=data['reting'],
                comment=data['comment'],
            )
            rating=prod.reviews.aggregate(avg_ratings=Avg('reting'))
            prod.ratings=rating['avg_ratings']
            prod.save()
        return Response({"massages":"Product review create"},status=status.HTTP_201_CREATED)
    #-------------------------Category-------------------------------#   
    @api_view(["GET"])
    def getProduct_by_category(request,Name):
        try:
           #query
            category=Categorys.objects.get(Name=Name)
            prod=Products.objects.filter(category=category)
            

            #serializer
            serializer=ProductSerializer(prod,many=True)
            
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        #Response
        return Response({
            "product":serializer.data,
        })