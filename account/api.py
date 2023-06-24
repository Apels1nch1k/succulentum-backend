from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import (
    TokenObtainPairView,

)
from shop.models.cart import CartUser
from .serializers import *

class MeUserApi(generics.RetrieveAPIView):
    serializer_class = UserDetail
    permission_classes = [permissions.IsAuthenticated]
    # queryset = User.objects.all()
    
    def get_object(self):
        return self.request.user
    
    
class RegisterAPI(APIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny,]
    
    def post(self, request):
        
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=serializer.data.get('username'))
            CartUser.objects.create(user=user, pcart=None)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AllOrderUser(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrderSerializer
    
    def get_queryset(self):
        user_id = self.request.user.id
        return Order.objects.filter(user=user_id).order_by('-created')
    
    
class TokenObtainPairView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny,]


    