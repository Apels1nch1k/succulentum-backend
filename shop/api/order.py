from rest_framework import generics,permissions, filters
from shop.models.order import Order, OrderProduct
from shop.serializers import OrderSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from yookassa import  Payment
from django.conf import settings

# print(settings.CORS_ALLOWED_ORIGINS )



class CreateOrder(APIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]
    
    
    def post(self, request, format=None):

        orders = self.request.data
        orders['user'] = self.request.user.id
        serializer = OrderSerializer(data=orders)
        if serializer.is_valid():
            order_data = serializer.validated_data
            products_data = order_data.pop('products')
            # Создание экземпляра Order
            order = Order.objects.create(**order_data)
            
            # Создание экземпляров OrderProduct
            for product_data in products_data:
                OrderProduct.objects.create(order=order, **product_data)
            print(orders)
            payment = Payment.create({
                'amount': {
                    'value': str(orders['total_price']),
                    'currency': 'RUB'
                },
                'description': 'Оплата заказа №{}'.format(order.id),
                'confirmation': {
                    'type': 'redirect',
                    'return_url': settings.CORS_ALLOWED_ORIGINS[0]
                }
            })

            # Сохранение информации о платеже в модели Order
            order.payment_id = payment.id
            order.paid = payment.status == "pending"
            order.payment_confirmation_url = payment.confirmation.confirmation_url
            order.save()

            # Вернуть данные о созданном заказе и ссылку на платежную форму
            data = OrderSerializer(order).data
            data['payment_confirmation_url'] = order.payment_confirmation_url
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        