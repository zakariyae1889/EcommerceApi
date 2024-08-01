from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status
from .serializers import SingUpSerializer,ClientSerializer
from rest_framework.permissions import IsAuthenticated

@api_view(["POST"])
def  register(request):
    try:
        data=request.data
        user=SingUpSerializer(data=data)
        if user.is_valid():
            if not User.objects.filter(username=data["email"]).exists():
                user=User.objects.create(
                    username=data["email"],
                    first_name=data["first_name"],
                    last_name=data["last_name"],
                    email=data["email"],
                    password=make_password(data['password'])
                )
                return Response(
                    {
                    "message":"your account register susccessfuly"
                    },
                    status=status.HTTP_201_CREATED
                )
            else:
                return Response(
                    {
                    "message":"This User Already Exists"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(user.errors)
    except User.DoesNotExist:
        return Response(
        {
            "message":"This Email Already Exists"
        },
        status=status.HTTP_400_BAD_REQUEST
    )
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def CurrentUser(request):
    user=ClientSerializer(request.user)
    return Response(user.data)

