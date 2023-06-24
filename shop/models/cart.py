from django.db import models
from django.contrib.auth. models import User


class CartUser(models.Model):
    user = models.OneToOneField(to=User, related_name="cartUser", verbose_name="Корзина пользователя", on_delete=models.CASCADE)
    pcart = models.JSONField(null=True, blank=True)

