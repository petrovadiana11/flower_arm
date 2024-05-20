from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic import CreateView

from .forms import OrderForm
from .models import Cart, Order
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

class OrderListView(generic.ListView):
    model = Order

    def get(self, request):
        order_list = Order.objects.filter(active="False")
        return render(request, 'mywork/order_list.html', {'order_list': order_list})

def order_history(request):
    order_list = Order.objects.filter(active="True")
    return render(request, 'mywork/order_list.html', {'order_list': order_list})

def order_status(request, pk):
    get_order = Order.objects.get(pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=get_order)
        if form.is_valid():
            form.save()
            return redirect(reverse('order'))

    template = 'mywork/edit.html'
    context = {
        'get_order': get_order,
        'update': True,
        'form': OrderForm(instance=get_order)
    }
    return render(request, template, context)

def delete_order(request, pk):
    get_order = Order.objects.get(pk=pk)
    get_order.delete()
    return redirect(reverse('order'))

class OrderDetailView(generic.DetailView):
    model = Order

class OrderCreate(CreateView):
    template_name = 'cart/oformlenie_shop.html'
    form_class = OrderForm
    success_url = reverse_lazy('thanks_delivery')

