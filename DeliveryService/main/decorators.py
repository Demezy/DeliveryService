import datetime
from django.shortcuts import redirect
from .models import User

entry_count = {}


def check_session(func):
    def decorator(*args, **kwargs):
        if 'auth' not in args[0].session.keys():
            args[0].session['auth'] = 0
        if 'login' not in args[0].session.keys():
            args[0].session['login'] = None
        return func(*args, **kwargs)

    return decorator


def login_required(func):
    def decorator(*args, **kwargs):
        if args[0].session.get('auth'):
            try:
                user = User.objects.get(username=args[0].session['username'])
            except Exception as e:
                print(e)
                args[0].session['auth'] = 0
                return redirect('login')
            else:
                return func(user, *args, **kwargs)
        return redirect('login')

    return decorator
