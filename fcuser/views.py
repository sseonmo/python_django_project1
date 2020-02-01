from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import RegisterForm, LoginForm
# Create your views here.


def index(request):
    return render(request, 'index.html', {'email': request.session.get('user')})


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'


class LoginView(FormView):
    print("========== LoginView =============")
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    # 로그인 처리가 올바르게 처리된 후 호출됨
    def form_valid(self, form):
        print('form_valid 2')
        print('user email : [{}]'.format(form.email))
        self.request.session['user'] = form.email
        return super().form_valid(form)
