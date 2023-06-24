from rest_framework import generics,permissions, viewsets, mixins
from rest_framework.response import Response
from shop.models.cart import CartUser
from shop.serializers import CartSerializer
from rest_framework.views import APIView

class Cart(APIView):
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'post']

    def get(self, request):
        if self.request.user:
            queryset = CartUser.objects.filter(user=self.request.user.id)
            serializer = CartSerializer(queryset, many=True)
            return Response(data=serializer.data)
        else:
            return Response(data=None)

    def post(self, request, *args, **kwargs): 
        if  self.request.data:
            pcart = self.request.data['pcart']
        else:
            pcart = []  
        if self.request.user:
            CartUser.objects.filter(user=self.request.user.id).update(pcart=pcart)
            return Response(data=self.request.data)
        else:
            return Response(data=None)

