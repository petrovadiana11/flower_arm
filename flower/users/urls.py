from django.urls import path

from .views import password_reset_form, password_reset_done, password_reset_email, password_reset_confirm, \
    password_reset_complete, RegisterUser

urlpatterns = [
    path('user/register/', RegisterUser.as_view(), name='user_register'),
    path('password/reset/form/', password_reset_form, name='password_reset_form'),
    path('password/reset/done/', password_reset_done, name='password_reset_done'),
    path('password/reset/email/', password_reset_email, name='password_reset_email'),
    path('password/reset/confirm/', password_reset_confirm, name='password_reset_confirm'),
    path('password/reset/complete/', password_reset_complete, name='password_reset_complete'),

]