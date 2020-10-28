# from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Product, Order, User
from .decorators import check_session, login_required
from hashlib import sha256

# constants
COMPANY = "Delivery Service"


@check_session
def index(request):
    try:
        return render(request, "main/index.html", {"title": "LinkPage", "COMPANY": COMPANY})
    except Exception:
        return error(request)


@check_session
def shop_page(request):
    try:
        return render(request, "main/Shop.html",
                      {"title": "Shop", "products": Product.objects.all(), "COMPANY": COMPANY})
    except Exception:
        return error(request)


@check_session
def test_page(request, num=0):
    try:
        return render(request, "main/test.html",
                      {"title": "TEST PAGE!",
                       # "products": Product.objects.all(),
                       "COMPANY": COMPANY})

    except Exception:
        return error(request)


@check_session
def login(request):
    try:
        if request.method == 'GET':
            params = {
                'auth': request.session['auth'],
            }
            return render(request, 'main/login.html', params)
        else:
            login = request.POST['login']
            password_hash = sha256(bytes(request.POST['password'], 'utf-8')).hexdigest()
            # TODO: save hash in DB
            try:

                user = User.objects.get(username=login)
            except Exception as e:
                # print(e)
                params = {
                    'error': 'Failed to authenticate'
                }
                return render(request, 'main/login.html', params)
            else:
                if password_hash == user.password:
                    request.session['auth'] = 1
                    request.session['username'] = user.username
                    return redirect('home')
                else:
                    params = {
                        'error': 'Failed to authenticate',
                    }
                    return render(request, 'main/login.html', params)
    except Exception:
        return error(request)


@check_session
def error(request, error_msg=None):
    return render(request, "main/error.html", {"COMPANY": COMPANY, "error_msg": error_msg})


@check_session
def logout(request):
    try:
        request.session['auth'] = 0
        return redirect('login')
    except Exception:
        return error(request)


def manager(request):
    """manager handler"""
    if request.method == "POST":
        # print(request.POST, "#" * 15)
        for key in request.POST:
            # print(key)
            if key == 'csrfmiddlewaretoken':
                continue
            else:
                val = request.POST.get(key)
                current = Order.objects.get(id=int(key))
                current.courier = User.objects.get(username=val)
                current.save()

    return render(request, "main/manage_page.html",
                  {"COMPANY": COMPANY,
                   "orders": Order.objects.all(),
                   "couriers": User.objects.filter(user_type=0)
                   })


def courier(request, user, number):
    """courier handler"""
    if number is None:

        return render(request,
                      "main/courier.html",
                      {"COMPANY": COMPANY,
                       "title": "courier",
                       "orders": Order.objects.filter(courier=user)})
    else:
        return render(request, "main/courier.html", {
            "title": "courier",
            "COMPANY": COMPANY,
            "orders": Order.objects.filter(courier=user, id=int(number)),  # verification of courier's order

        })


@check_session
@login_required
def show_page(user: User, request, number=None):
    # try:
    if user.user_type == 1:
        return manager(request)
    elif user.user_type == 0:
        return courier(request, user, number)
    else:
        return error(request, "The administrator assigned you the wrong user type. ")

    # except Exception as e:
    #     return error(request, e)
