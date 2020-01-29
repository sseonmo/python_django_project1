from django.db import models

# Create your models here.


class Product(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=256, verbose_name='상품명')
    price = models.IntegerField(verbose_name='상품가격')
    description = models.TextField(verbose_name='상품설명')
    stock = models.IntegerField(verbose_name='재고')
    register_data = models.DateTimeField(
        auto_now_add=True, verbose_name='등록날짜')

    def __str__(self):
        return self.name

    # Meta
    class Meta:
        db_table = 'fastcampus_prodcut'
        verbose_name = '상품'
        verbose_name_plural = '상품'
