from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import RegisterForm, LoginForm
from .models import Fcuser
from django.contrib.auth.hashers import check_password, make_password  # 암호화확인, 암호화

# Create your views here.


def index(request):
	return render(request, 'index.html', {'email': request.session.get('user')})

class RegisterView(FormView):
	template_name = 'register.html'
	form_class = RegisterForm
	success_url = '/'

	# 유효성검사가 종료되었을때 호출됨
	def form_valid(self, form):
		fcuser = Fcuser(
			email=form.data.get('email')
			, password=make_password(form.data.get('password'))
			, level='user'
		)

		fcuser.save()
		return super().form_valid(form)


class LoginView(FormView):
	print("========== LoginView =============")
	template_name = 'login.html'
	form_class = LoginForm
	success_url = '/'

	# 로그인 처리가 올바르게 처리된 후 호출됨
	def form_valid(self, form):
		print('form_valid 2')
		print('user email : [{}]'.format(form.data.get('email')))
		self.request.session['user'] = form.data.get('email')
		return super().form_valid(form)

def logout(request):
	if 'user' in request.session:
		del (request.session['user'])

	return redirect('/login/')
