from django.db import models
from django.contrib.auth.models import User
from mywork.models import Product

# Create your models here.
class CartQueryset(models.QuerySet):
    def total_price(self):
        return sum(cart.product_price() for cart in self)


class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь')
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')
    session_key = models.CharField(max_length=30, null=True, blank=True)
    tamestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзина"

    objects = CartQueryset().as_manager()

    def product_price(self): #подсчет цен товаров по количеству
        return round(self.product.price * self.quantity, 2)

    def __str__(self):
        return f'Корзина {self.user.username} | Товар {self.product.name} | Количество {self.quantity}'