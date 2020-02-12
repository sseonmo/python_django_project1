from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):

	class Meta:
		model = Product
		# fiedls 를 명시하지 않으면 기본적으로 모델의 전체 필드를 가져온다.
		fields = '__all__'