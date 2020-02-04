from django.shortcuts import redirect
from fcuser.models import Fcuser


def login_required(func):

    def wrap(request, *args, **kwargs):
        user = request.session.get('user')
        # None 이거나 빈값이면
        if user is None or not user:
            return redirect('/login')

        print('login_require')
        return func(request, *args, **kwargs)

    return wrap


def admin_required(func):

    def wrap(request, *args, **kwargs):
        user = request.session.get('user')
        # None 이거나 빈값이면
        if user is None or not user:
            return redirect('/login')

        user = Fcuser.objects.get(email=str(user))
        if user.level != 'admin':
            return redirect('/')

        print('login_require')
        return func(request, *args, **kwargs)

    return wrap
