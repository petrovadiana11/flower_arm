from django.shortcuts import render, redirect
from .models import Cart
from mywork.models import Product


# Create your views here.
def cart_add(request, pk):
    product = Product.objects.get(pk=pk)
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)
    return redirect(request.META['HTTP_REFERER'])


def cart_change(request, product_slug):
    ...

def cart_remove(request, pk):
    cart = Cart.objects.get(pk=pk)
    cart.delete()
    return redirect(request.META['HTTP_REFERER'])


