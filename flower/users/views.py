from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from .forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy, reverse


class UserLoginView(LoginView):
    template_name = 'users/login.html'
class RegisterUser(CreateView):
    template_name = 'users/registr.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

def password_reset_form(request):
    return render(request, 'registration/password_reset_form.html')

def password_reset_done(request):
    return render(request, 'registration/password_reset_done.html')

def password_reset_email(request):
    return render(request, 'registration/password_reset_email.html')

def password_reset_confirm(request):
    return render(request, 'registration/password_reset_confirm.html')

def password_reset_complete(request):
    return render(request, 'registration/password_reset_complete.html')



