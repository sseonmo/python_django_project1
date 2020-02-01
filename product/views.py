from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .models import Product
from .forms import RegisterForm
from order.forms import RegisterForm as OrderForm
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

    # context custom 함수
    def get_context_data(self, **kwargs):
        # 기본적으로 super를 호출해서 기본을 작업 후 작업을 진행한다.
        context = super().get_context_data(**kwargs)
        # form변수에 OrderForm 추가
        # View class 이기때문에 session가 존재한다.
        print("===== get_context_data ======")
        context['form'] = OrderForm(self.request)
        return context
