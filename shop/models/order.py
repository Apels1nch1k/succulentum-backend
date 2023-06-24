from django.db import models
from django.contrib.auth. models import User
from .product import Product

class StatusOrder(models.TextChoices):
    OrderProcessing =  'Обработка заказа'
    OrderDelivery =   'Доставка заказа'
    OrderCompleted =  'Заказ завершён'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Покупатель", null=True)
    city = models.CharField(max_length=100, verbose_name="Город")
    street = models.CharField(max_length=255, verbose_name="Улица")
    house_number = models.CharField(max_length=255, verbose_name="Номер дома")
    apartment_number = models.CharField(max_length=255, verbose_name="Номер квартиры")
    created = models.DateTimeField(auto_now_add=True,verbose_name='Добавление')
    payment_id = models.CharField(max_length=255, verbose_name="ID оплаты")
    updated = models.DateTimeField(auto_now=True,verbose_name='Изменение')
    paid = models.BooleanField(default=False, verbose_name='Оплата')
    status_order = models.CharField(StatusOrder, choices=StatusOrder.choices, default=StatusOrder.OrderProcessing, max_length=50)
    payment_confirmation_url = models.TextField()
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        
    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(product.get_cost() for product in self.products.all())
    
    def get_product_all(self):
        return self.order_products.all()
    
class OrderProduct(models.Model):
    order = models.ForeignKey(Order, related_name="products", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="order_products", on_delete=models.CASCADE)
    price =models.IntegerField()
    quantity = models.PositiveSmallIntegerField(default=1)
    
    
    def __str__(self) -> str:
        return str(self.id)
    
    def get_cost(self):
        return self.price * self.quantity