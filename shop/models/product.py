from django.db import models
from .category import Category


class Product(models.Model):
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    name = models.CharField(max_length=120, verbose_name="Название")
    image = models.ImageField(upload_to="product/%Y/%m/%d", blank=True)
    description = models.TextField(max_length=1500, blank=True,verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    available = models.BooleanField(default=True,verbose_name='Наличие')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Добавление')
    uploaded = models.DateTimeField(auto_now=True,verbose_name='Изменение')
    stock = models.IntegerField(verbose_name='Количество на складе')
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
    
    def __str__(self) -> str:
        return self.name