from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import RegisterForm
from .models import Order

# Create your views here.


class OrderCreate(FormView):
    form_class = RegisterForm
    success_url = '/product/'

    # is_valid을 실패했을때
    def form_invalid(self, form):
        return redirect('/product/'+str(form.product))

    # 폼을 생성할때 어떤 인자값을 전달해서 만들지 결정
    def get_form_kwargs(self, **kwargs):
        print("===== get_from_kwargs ======")
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })

        return kw
