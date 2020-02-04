from django.db import models

# Create your models here.


class Order(models.Model):

    # app에 class로 명시해준다.
    objects = models.Manager()

    # on_delete은 삭제되었을때 어떻게 할건지 / models.CASCADE : 원본이 삭제되면 같이 삭제
    fcuser = models.ForeignKey(
        'fcuser.FcUser', on_delete=models.CASCADE, verbose_name='사용자')
    product = models.ForeignKey(
        'product.Product', on_delete=models.CASCADE, verbose_name='상품')
    quantity = models.IntegerField(verbose_name='수량')
    register_date = models.DateTimeField(
        auto_now_add=True, verbose_name='등록날짜')

    def __str__(self):
        return '{}  {}'.format(str(self.fcuser), str(self.product))

    # Meta
    class Meta:
        db_table = 'fastcampus_order'
        verbose_name = '주문'
        verbose_name_plural = '주문'
