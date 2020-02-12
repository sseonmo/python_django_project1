from django import forms
from .models import Order
from product.models import Product
from fcuser.models import Fcuser
from django.db import transaction


class RegisterForm(forms.Form):

    # Session은 request에 존재하므로 Form에서는 사용 불가.
    # 따라서 FormView의 생성자가 request를 포함하도록 변경

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    quantity = forms.IntegerField(
        error_messages={
            'required': '수량을 입력해주세요.'
        },
        label='수량'
    )

    product = forms.IntegerField(
        widget=forms.HiddenInput
    )

    def clean(self):
        print("==== order form clean ==== ")
        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity')
        product = cleaned_data.get('product')
        fcuser = self.request.session.get('user')

        if not (quantity and product and fcuser):
            self.add_error('quantity', '값이 없습니다.')
            self.add_error('product', '값이 없습니다.')
