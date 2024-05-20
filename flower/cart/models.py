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

def func():
    nm = Product.objects.all()
    nm1 = 1
    for i1 in nm:
        if i1.id > nm1:
            nm1 = i1.id
    nm1 = nm1 + 1
    nn = '000' + str(nm1)
    return nn

class Order(models.Model):
    shop_code = models.CharField(max_length=20, unique=True, default=func, verbose_name='Номер заявки')
    name = models.CharField(max_length=100, help_text="Введите имя и фамилию получателя",
                            verbose_name="Имя и фамилия получателя")
    adres = models.CharField(max_length=200, help_text="Введите адрес доставки",
                            verbose_name="Адрес", blank=True)
    number = models.CharField(help_text="Введите номер телефона получателя",
                            verbose_name="Номер телефона получателя")
    cart = models.ManyToManyField(Cart, null=True,blank=True,
                                help_text="Товар", verbose_name="Товар")
    published = models.DateTimeField(auto_now_add=True, db_index=True, null=True,
                                     verbose_name="Дата заказа")
    date_of_receipt = models.DateTimeField(verbose_name="Дата и время получения")
    message = models.CharField(max_length=200, blank=True, help_text="Введите дополнительную информацию",
                            verbose_name="Дополнительная информация")
    active = models.BooleanField(default=False, verbose_name="")

    def __str__(self):
        return self.name

    def get_absolute_path(self):
        return reverse('order-detail', args=[str(self.id)])

    class Meta:
        verbose_name_plural = "Заказы"