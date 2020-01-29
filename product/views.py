from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .models import Product
from .forms import RegisterForm
# Create your views here.


class ProductList(ListView):
    model = Product
    template_name = 'product.html'
    # object 명칭 지정
    context_object_name = 'product_list'


class ProductCreate(FormView):
    template_name = 'register_product.html'
    form_class = RegisterForm
    success_url = '/product/'


class ProductDeatil(DetailView):
    template_name = 'product_detail.html'
    queryset = Product.objects.all()
    # model = Product
    context_object_name = 'product'
