import django_filters
from .models import *

class ProductFilter(django_filters.FilterSet):
    keyword=django_filters.filters.CharFilter(field_name="Name",lookup_expr="icontains")
    minPirce=django_filters.filters.NumberFilter(field_name="Price" or 0 ,lookup_expr="gte")
    maxPrice=django_filters.filters.NumberFilter(field_name="Price" or 1000 ,lookup_expr="lte")
    class Meta:
        model=Products
        fields=("keyword","Price","color","size")