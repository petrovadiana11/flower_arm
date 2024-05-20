
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
    structure = models.CharField(max_length=50, verbose_name="Состав букета")
    massa = models.CharField(max_length=50, verbose_name="Вес")
    published = models.DateTimeField(auto_now_add=True, db_index=True,
                                     verbose_name="Дата выставки")

    def __str__(self):
        return self.name

    def get_absolute_path(self):
        return reverse('product-detail', args=[str(self.id)])

    class Meta:
        verbose_name_plural = "Товары"








