from rest_framework import serializers
from .models import ShoppineAddress


class ShoppineAddressSerializers(serializers.ModelSerializer):
    class Meta:
        model=ShoppineAddress
        fields="__all__"
