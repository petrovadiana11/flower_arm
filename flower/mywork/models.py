
from django.db import models
from django.urls import reverse


# Create your models here.
class Help(models.Model):
    name = models.CharField(max_length=50, verbose_name="Ваше имя")
    number = models.CharField(max_length=11, verbose_name="Ваш номер телефона")
    message = models.TextField(verbose_name="Обращение")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Обращения"



class Category(models.Model):
    name = models.CharField(max_length=200,
                            verbose_name="Категория товара")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name="Название товара")
    kod_product = models.CharField(max_length=50, verbose_name="Код товара")
    price = models.IntegerField(verbose_name="Цена товара")
    count = models.IntegerField(verbose_name="Количество товара")
    category = models.ForeignKey('Category', on_delete=models.CASCADE,
                            verbose_name="Категория товара")
    cover = models.ImageField(upload_to='images/', null=True,
                              verbose_name="Изображение")
    info = models.TextField(max_length=1000,
                           verbose_name="Информация о товаре")
    published = models.DateTimeField(auto_now_add=True, db_index=True,
                                     verbose_name="Дата выставки")

    def __str__(self):
        return self.name

    def get_absolute_path(self):
        return reverse('product-detail', args=[str(self.id)])

    class Meta:
        verbose_name_plural = "Товары"


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
    product = models.ForeignKey('Product', on_delete=models.CASCADE,
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



