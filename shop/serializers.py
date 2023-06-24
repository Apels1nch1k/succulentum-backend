from rest_framework import serializers
from .models.category import Category
from .models.product import Product
from .models.order import Order, OrderProduct
from .models.cart import CartUser
from .models.comment import Comment
from .models.slider import Slider
from django.contrib.auth. models import User

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    class Meta:
        model = User
        fields = ['id', 'username']

        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
             
class ProductSerializerDetail(serializers.ModelSerializer):
    created = serializers.DateTimeField(format='%d/%m/%y, %H:%M:%S')
    uploaded = serializers.DateTimeField(format='%d/%m/%y, %H:%M:%S')
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    
    class Meta:
        model = Product
        fields = ['id', "name", 'price', 'image', 'category']



class OrderProduct(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ('product', 'price', 'quantity')
        
class OrderSerializer(serializers.ModelSerializer):
    products = OrderProduct(many=True)
    class Meta:
        model = Order
        fields = ('id', 'user', 'city', 'street', 'house_number', 'apartment_number', 'products')
        
        
class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartUser
        fields = ['pcart', ]
        
class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    created_date = serializers.DateTimeField(format='%d/%m/%y, %H:%M:%S',  read_only=True)
    class Meta:
        model = Comment
        fields = "__all__"
        
    def create(self, validated_data):
        text = validated_data.pop('text')
        product = validated_data.pop('product')
        user = validated_data.pop('user')
        user = User.objects.get(username=user['username'])
        comment = Comment.objects.create(text=text, user=user, product=product)
        return comment
        
class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = '__all__'