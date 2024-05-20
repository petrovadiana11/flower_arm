from django.urls import path
from .views import cart_add, cart_change, cart_remove, OrderListView, order_history, order_status, delete_order, \
    OrderDetailView, OrderCreate

urlpatterns = [
    path(r'^cart_add/(?P<pk>\d+)$/', cart_add, name='cart_add'),
    path('cart_change/<slug:product_slug>/', cart_change, name='cart_change'),
    path('cart_remove/<int:pk>/', cart_remove, name='cart_remove'),
    path('order/', OrderListView.as_view(), name='order'),
    path('order/history/', order_history, name='order_history'),
    path('status/<int:pk>/', order_status, name='order_status'),
    path('delete/order/<int:pk>/', delete_order, name='delete_order'),
    path(r'^order/(?P<pk>\d+)$', OrderDetailView.as_view(), name='order-detail'),
    path('order/create/', OrderCreate.as_view(), name='order-create'),

]