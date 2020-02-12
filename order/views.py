from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from .forms import RegisterForm
from .models import Order
from fcuser.decorators import login_required
from django.db import transaction
from product.models import Product
from fcuser.models import Fcuser
# Create your views here.


@method_decorator(login_required, name='dispatch')
class OrderCreate(FormView):
    form_class = RegisterForm
    success_url = '/product/'

    # is_valid을 실패했을때
    def form_invalid(self, form):
        return redirect('/product/'+str(form.data.get('product')))

    def form_valid(self, form):
        print("===== OrderCreate  ::  form_valid  ======")
        product = form.data.get('product')
        quantity = int(form.data.get('quantity'))
        fcuser = self.request.session.get('user')
        with transaction.atomic():
            prod = Product.objects.get(pk=product)
            order = Order(
                quantity=quantity, product=Product.objects.get(pk=product), fcuser=Fcuser.objects.get(email=fcuser)
            )
            order.save()
            prod.stock -= quantity
            prod.save()

        return super().form_valid(form)

    # 폼을 생성할때 어떤 인자값을 전달해서 만들지 결정
    # POST or PUT 일때 요청데이터도 제공된다.
    def get_form_kwargs(self, **kwargs):
        print("===== get_from_kwargs ======")
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })

        return kw


@method_decorator(login_required, name='dispatch')
class OrderList(ListView):
    # model = Order
    template_name = 'order.html'
    context_object_name = 'order_list'

    def get_queryset(self, **kwargs):
        queryset = Order.objects.filter(
            fcuser__email=self.request.session.get('user'))
        return queryset
