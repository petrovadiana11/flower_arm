from django.contrib import admin
from .models import Help, Category, Product, Order

# Register your models here.

admin.site.register(Help)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
