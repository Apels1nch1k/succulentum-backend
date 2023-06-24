from rest_framework import serializers
from .models import *
from shop.models.order import Order,OrderProduct
from shop.models.product import Product
from django.contrib.auth.models import User
from backend.exceptions import CustomAPIException

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True)
    password_repeat = serializers.CharField(max_length=128, write_only=True)
    class Meta:
        model = User
        fields = ['username','email', 'password', 'password_repeat']
        
    def validate(self, data):
        # Ensure the passwords match
        if data['password'] != data['password_repeat']:
            raise CustomAPIException({"password_repeat":["Пароли не совпадают",]})

        # Validate the email address
        email = data.get('email', None)
        if email and User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Пользователь с таким адресом электронной почты уже существует")
        
        return data
    
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
    
class UserDetail(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_superuser']
        
        

class ProductSerializerSmall(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', "name",'image'] 
               
class OrderProductSerializer(serializers.ModelSerializer):
    
    product = ProductSerializerSmall()
    
    class Meta:
        model = OrderProduct
        fields = ('id', 'product', 'price', 'quantity'  ) 

class OrderSerializer(serializers.ModelSerializer):
    total_cost = serializers.SerializerMethodField()
    products = OrderProductSerializer(many=True)
    created = serializers.DateTimeField(format='%d/%m/%y, %H:%M:%S')
    updated = serializers.DateTimeField(format='%d/%m/%y, %H:%M:%S')
    class Meta:
        model = Order
        fields = ('id', 'city','user', 'street', 'house_number', 'apartment_number', 'created', 'updated', 'paid', 'status_order', 'total_cost', 'products')

    def get_total_cost(self, obj):
        return obj.get_total_cost()

    # def get_products(self, obj):
    #     products = []
    #     for order_product in obj.order_products.all():
    #         product_data = {
    #             'name': order_product.product.name,
    #             'quantity': order_product.quantity,
    #             'price': order_product.price
    #         }
    #         products.append(product_data)
    #     return products