from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'number_phone', 'last_name', 'email', 'password1', 'password2')

    username = forms.CharField()
    last_name = forms.CharField()
    number_phone = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    # username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    # number_phone = forms.CharField(label='Номер телефона', widget=forms.NumberInput(attrs={'class': 'form-input'}))
    # email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    # password1 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    # password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))