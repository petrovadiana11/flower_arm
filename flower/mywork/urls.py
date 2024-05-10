
from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import index, ProductListView, teh_pod, ProductCreate, CategoryCreate, password_reset_done, \
    password_reset_email, \
    password_reset_confirm, password_reset_complete, password_reset_form, RegisterUser, UserLoginView, HelpCreate, \
    OrderListView, Search, OrderDetailView, update_product, delete_product, order_history, order_status, delete_order, \
    FilterProduct, main_arm, korzina_shop, oformlenie_shop, thanks_delivery, profil, o_nas, \
    ProductDetailView, filters, UserLogoutView

urlpatterns = [
    path('', index, name='index'),
    path('filters/', filters, name='filters'),
    path(r'^product/(?P<pk>\d+)$', ProductDetailView.as_view(), name='product-detail'),
    path('korzina_shop', korzina_shop, name='korzina_shop'),
    path('oformlenie_shop', oformlenie_shop, name='oformlenie_shop'),
    path('thanks_delivery', thanks_delivery, name='thanks_delivery'),
    path('profil', profil, name='profil'),
    path('o_nas', o_nas, name='o_nas'),
    path('main_arm', main_arm, name='main_arm'),
    path('product/', ProductListView.as_view(), name='product'),
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
    path('user/register/', RegisterUser.as_view(), name='user_register'),
    path('send/help/', HelpCreate.as_view(), name='send_help'),
    path('teh_pod/', teh_pod, name='teh_pod'),
    path('password/reset/form/', password_reset_form, name='password_reset_form'),
    path('password/reset/done/', password_reset_done, name='password_reset_done'),
    path('password/reset/email/', password_reset_email, name='password_reset_email'),
    path('password/reset/confirm/', password_reset_confirm, name='password_reset_confirm'),
    path('password/reset/complete/', password_reset_complete, name='password_reset_complete'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),




]