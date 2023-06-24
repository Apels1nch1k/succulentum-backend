from rest_framework import generics,permissions, filters 
from  rest_framework.response import Response
from shop.models.comment import Comment
from shop.models.product import Product
from shop.serializers import CommentSerializer
from django.shortcuts import get_object_or_404
from shop.models.comment import Comment
from rest_framework.views import APIView
from django.contrib.auth. models import User


class CommentListApi(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]
    
    
    def get_queryset(self):
        product_id = self.kwargs.get('comment_id')
        return Comment.objects.filter(product=product_id)
    

    

class CommentCreateApi(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]    
    http_method_names = ['post', ]
    serializer_class = CommentSerializer
    def post(self,request):
        print(self.request.user.username)
        commentUser = self.request.data
        commentUser["user"] = {
            "username" : self.request.user.username
            }

        serializer = self.serializer_class(data=commentUser)
        
        if serializer.is_valid():
            print(serializer)
            serializer.save()
            return Response(data=serializer.data, status=201)
        
            
        return Response(data=serializer.errors, status=400)