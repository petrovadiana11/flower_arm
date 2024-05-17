from django.urls import path
from .views import cart_add, cart_change, cart_remove

urlpatterns = [
    path(r'^cart_add/(?P<pk>\d+)$/', cart_add, name='cart_add'),
    path('cart_change/<slug:product_slug>/', cart_change, name='cart_change'),
    path('cart_remove/<int:pk>/', cart_remove, name='cart_remove'),

]