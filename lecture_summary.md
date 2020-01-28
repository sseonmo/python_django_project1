##  class has no objects member 에러 
1. 파이썬의 오류를 찾아주는 라이브러리 pylint-django 설치
```python
# 1.설치
pip install pylint_django

# 2. vscode 사용자 설정 추가
"""
"python.linting.pylintArgs": [
    "--load-plugins=pylint_django"
]
"""
```
1. 오류가 발생하는 모델수정
```python
class Fcuser(models.Model):
    # 추가
    objects = models.Manager()
    email = models.EmailField(verbose_name='이메일')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    register = models.DateField(auto_now_add=True, verbose_name='등록날짜')
    ...
```

## [Humanize 사용](https://docs.djangoproject.com/en/2.2/ref/templates/builtins/)
1. 휴머나이즈 필터는 날짜, 숫자 등을 사람 눈에 더 친숙하게 바꿔주는 필터를 제공
1. 해당 필터를 사용하기 위해선 settings.py에 `django.contrib.humanize`를 app으로 등록필요
1. 사용을 원하는 html 파일에서 {% load humanize %}를 통해 로드

```python
# setting.py

INSTALLED_APPS = [
    ...
    # humanize filter를 사용하기 위해 app 사용등록 필요함
    'django.contrib.humanize',  
]
```
```html
<!-- some.html -->
...
{% load humanize %}
...
<!-- ilter를 적용할 때에는 | 를 입력 후 원하는 filter를 적용 -->
<!--  intcomma는 숫자 3개마다 ,를 붙여주는 filter -->
<td>{{ product.price|intcomma }} 원</td>
<!--  date는 날짜관련 filter -->
<td>{{ product.register_data|date:"Y-m-d h:i" }}</td>
```


## webeditor
- [summernote](https://summernote.org/) : 간단하게 적용가능


## TemplateView 

```python
# urls.py
# MyView라는 클래스 뷰를 사용

from django.conf.urls import url
from myapp.views import AboutView

urlpatterns = [
	url(r'^about/$', AboutView.as_view())
	]
"""
- as_view()
1. as_view()는 url 해석기에서 class view로 진입하기 위한 매소드
2. 클래스의 인스턴스를 생성하고 그 인스턴스의 dispatch() 매소드를 호출
3. dispatch() 메소드는 요청을 검사하여 HTTP 요청 메소드를 알아낸 다음, 인스턴스 내에 해당 이름을 갖는 메소드로 요청을 중계한다
4. 요청에 맞는 메소드가 없으면 에러 발생
"""    
---

# views.py
# /about/ url로 요청이 들어오면 about.html을 보여주는 TemplateView

from django.views.generic import TemplateView

class AboutView(TemplateView):
	template_name = 'about.html'

``` 

## FormView 
```python
# views.py
# MyForm 폼클래스를 적용하여 about.html을 보여주고

from django.views.generic.edif import FormView
 
class AboutView(FormView):
    # MyForm를 forms에 정의해야함
    form_class = MyForm 
    template_name = 'about.html'
    success_url = 'thanks'
 
    def form_valid(self, form):
        # cleaned_data로 관련 로직 처리
        return super(MyFormView, self).form_valid(form)
```
- form_class : 사용자에 보여줄 폼을 정의한 forms.py 파일 내의 클래스명
- template_name : 폼을 포함하여 렌더링할 템플릿 파일 이름
- success_url : MyFormView 처리가 정상적으로 완료되었을 때 리다이렉트시킬 URL
- form_valid() 함수 : 유효한 폼 데이터로 처리할 로직 코딩, 반스시 super() 함수 호출.

## ListView
- 글 목록이 전체를 표시하거나, 특정 DB table의 전체를 표시할 대 활용할 수 있다.
- 리스트가 테이블의 모든 레코드인 경우 모델 클레스만 지정하면 된다.
```python

# urls.py
from product.views import ProductList

urlpatterns = [
    path('product/', ProductList.as_view()),
]

---

# views.py
from django.views.generic import ListView
from .models import Product

class ProductList(ListView):    
    # 모델지정
    model = Product
    # 사용할 template 파일
    template_name = 'product.html'
    # object 명칭 지정
    # default context : object_list
    context_object_name = 'product_list'

```
```html
...
<!-- context 사용 -->
{% for product in product_list %}
<tr>
    <td scope="row">{{ product.id }}</td>
    <td>{{ product.name }}</td>
    <td>{{ product.price|intcomma }} 원</td>
    <td>{{ product.register_data|date:"Y-m-d h:i" }}</td>
</tr>
{% endfor %}
...
```