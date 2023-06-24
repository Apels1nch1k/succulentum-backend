from rest_framework import generics,permissions, filters
from  rest_framework.response import Response
from ..models import *
from ..serializers import *

class CategoryListApi(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]