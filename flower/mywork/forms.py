
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Product, Category, Help, Order
from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'kod_product', 'price', 'count', 'category', 'cover', 'info')

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('active',)

class HelpForm(ModelForm):
    class Meta:
        model = Help
        fields = ('name', 'number', 'message')

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
