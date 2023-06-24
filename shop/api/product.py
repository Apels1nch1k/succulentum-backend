from rest_framework import generics,permissions, filters
from  rest_framework.response import Response
from ..models import *
from ..serializers import *


class ProductListApi(generics.ListAPIView):
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductSerializer
    search_fields = ['=category__id', '$name', ]
    filter_backends = [filters.SearchFilter]
    permission_classes = [permissions.AllowAny]
    

    
class ProductDetailApi(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializerDetail
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', ]