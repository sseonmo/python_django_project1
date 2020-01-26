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