from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from django.views import generic
from .forms import ProductForm, CategoryForm, HelpForm, OrderForm
from .models import Product, Order, Category
from django.views.decorators.http import require_POST
from django.views.generic import ListView
from django.http import HttpResponseRedirect



# Create your views here.

class ProductDetailView(generic.DetailView):
    category = Category.objects.all()
    model = Product

def korzina_shop(request):
    category = Category.objects.all()
    return render(request, "cart/korzina_shop.html", context={'category': category},)


def oformlenie_shop(request):
    category = Category.objects.all()
    return render(request, "mywork/oformlenie_shop.html", context={'category': category},)

def thanks_delivery(request):
    category = Category.objects.all()
    return render(request, "mywork/thanks_delivery.html", context={'category': category},)

def profil(request):
    category = Category.objects.all()
    return render(request, "mywork/profil.html", context={'category': category},)

def o_nas(request):
    category = Category.objects.all()
    if request.method == 'POST':
        form = HelpForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('../')
            except:
                print(form.cleaned_data)
                form.add_error(None, 'ошибка')
    else:
        form = HelpForm()
    return render(request, "mywork/o_nas.html", context={'category': category,
                                                         'form': form},)

def main_arm(request):
    num_product = Product.objects.all().count()
    num_order = Order.objects.filter(active="False").count()
    num_category = Category.objects.all().count()
    num_user = User.objects.all().count()
    return render(request, "mywork/main_arm.html",context={'num_product': num_product,
                           'num_order': num_order,
                            'num_user': num_user,
                            'num_category': num_category},)

class CategorySearch:
    def get_category(self):
        return Category.objects.all()

class FilterProduct(ListView, CategorySearch):
    def get_queryset(self):
        queryset = Product.objects.filter(category__in=self.request.GET.getlist("category"))
        return queryset

class Search(ListView):
    def get_queryset(self):
        return Product.objects.filter(name__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}'
        return context
class ProductListView(generic.ListView, CategorySearch):
    model = Product
def product_arm(request):
    product = Product.objects.all()
    return render(request, "mywork/product_arm.html", context={'product_list': product},)
def update_product(request, pk):
    get_product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=get_product)
        if form.is_valid():
            form.save()
            return redirect(reverse('product'))

    template = 'mywork/add_product.html'
    context = {
        'get_product': get_product,
        'update': True,
        'form': ProductForm(instance=get_product)
    }
    return render(request, template, context)

def delete_product(request, pk):
    get_product = Product.objects.get(pk=pk)
    get_product.delete()
    return redirect(reverse('product'))

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

class CategoryCreate(CreateView):
    template_name = 'mywork/add_category.html'
    form_class = CategoryForm
    success_url = reverse_lazy('product')

class ProductCreate(CreateView):
    template_name = 'mywork/add_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('product')



class HelpCreate(CreateView):
    template_name = 'mywork/send_help.html'
    form_class = HelpForm
    success_url = reverse_lazy('teh_pod')


def teh_pod(request):
    return render(request, "mywork/tehnical.html")



def logout_user(request):
    return redirect(request.META['HTTP_REFERER'])

