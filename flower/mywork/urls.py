import django
from django.contrib.auth import logout
from django.urls import path
from .views import ProductListView, teh_pod, ProductCreate, CategoryCreate, HelpCreate, \
    Search, update_product, delete_product,  \
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
    path('search/', Search.as_view(), name='search'),
    path('update/<int:pk>/', update_product, name='update_product'),
    path('delete/product/<int:pk>/', delete_product, name='delete_product'),
    path(r'^product/create/$', ProductCreate.as_view(), name='product_create'),
    path('category/create/', CategoryCreate.as_view(), name='category_create'),
    path('send/help/', HelpCreate.as_view(), name='send_help'),
    path('teh_pod/', teh_pod, name='teh_pod'),






]