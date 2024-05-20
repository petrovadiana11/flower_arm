import django
from django.contrib.auth import logout
from django.urls import path
from .views import ProductListView, teh_pod, ProductCreate, CategoryCreate, HelpCreate, \
    OrderListView, Search, OrderDetailView, update_product, delete_product, order_history, order_status, delete_order, \
    FilterProduct, main_arm, korzina_shop, oformlenie_shop, thanks_delivery, profil, o_nas, \
    ProductDetailView, product_arm


urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path(r'^product/(?P<pk>\d+)$', ProductDetailView.as_view(), name='product-detail'),
    path('korzina_shop/', korzina_shop, name='korzina_shop'),
    path('oformlenie_shop/', oformlenie_shop, name='oformlenie_shop'),
    path('thanks_delivery/', thanks_delivery, name='thanks_delivery'),
    path('profil/', profil, name='profil'),
    path('product/', product_arm, name='product'),
    path('o_nas/', o_nas, name='o_nas'),
    path('main_arm/', main_arm, name='main_arm'),
    path('filter/', FilterProduct.as_view(), name='filter'),
    path('order/', OrderListView.as_view(), name='order'),
    path('order/history/', order_history, name='order_history'),
    path('status/<int:pk>/', order_status, name='order_status'),
    path('delete/order/<int:pk>/', delete_order, name='delete_order'),
    path(r'^order/(?P<pk>\d+)$', OrderDetailView.as_view(), name='order-detail'),
    path('search/', Search.as_view(), name='search'),
    path('update/<int:pk>/', update_product, name='update_product'),
    path('delete/product/<int:pk>/', delete_product, name='delete_product'),
    path(r'^product/create/$', ProductCreate.as_view(), name='product_create'),
    path('category/create/', CategoryCreate.as_view(), name='category_create'),
    path('send/help/', HelpCreate.as_view(), name='send_help'),
    path('teh_pod/', teh_pod, name='teh_pod'),






]