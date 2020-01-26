from django.contrib import admin
from .models import Fcuser

# Register your models here.


class FcuserAdmin(admin.ModelAdmin):
    # 튜플로 인식해야 하기때문에 하나일때는 마지막에 ','를 꼭 포함해야함
    list_display = ('email',)


admin.site.register(Fcuser, FcuserAdmin)
