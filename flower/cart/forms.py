from django.forms import ModelForm, TextInput, Textarea
from .models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('active','name', 'adres', 'number', 'date_of_receipt','message' )

        widgets = {
            'name': TextInput(attrs={'placeholder': 'Введите имя...'}),
            'adres': TextInput(attrs={'placeholder': 'Введите адрес...'}),
            'number': TextInput(attrs={'placeholder': 'Введите номер телефона...'}),
            'date_of_receipt': TextInput(attrs={'placeholder': 'Предпочитаемная дата'}),
            'message': Textarea(attrs={'placeholder': 'Сообщение...'}),
        }