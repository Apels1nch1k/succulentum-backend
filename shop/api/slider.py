from rest_framework import generics,permissions, filters
from shop.serializers import SliderSerializer
from shop.models import Slider


class SliderListApi(generics.ListAPIView):
    serializer_class = SliderSerializer
    permission_classes = [permissions.AllowAny]
    
    
    def get_queryset(self):
        return Slider.objects.all()