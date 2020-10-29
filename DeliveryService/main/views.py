# from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Product, Order, User
from .decorators import check_session, login_required
from hashlib import sha256
from .district_handler import check_location

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
                "title": "login",
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
                    'error': 'Failed to authenticate',
                    "title": "login",
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
                        "title": "login",
                    }
                    return render(request, 'main/login.html', params)
    except Exception:
        return error(request)


@check_session
def error(request, error_msg=None):
    return render(request, "main/error.html", {"COMPANY": COMPANY, "title": "Error", "error_msg": error_msg})


@check_session
def logout(request):
    try:
        request.session['auth'] = 0
        return redirect('login')
    except Exception:
        return error(request)


def manager(request, number):
    """manager handler"""
    if request.method == "POST":
        current = Order.objects.get(id=int(number))
        if request.POST.get("status_upd"):
            current.status = int(request.POST.get("status_upd"))

        if request.POST.get("courier_upd"):
            current.courier = User.objects.get(username=request.POST.get("courier_upd"))
        current.save()

    return render(request, "main/manage_page.html",
                  {"COMPANY": COMPANY,
                   "title": "Manage",
                   "orders": Order.objects.all(),
                   "couriers": User.objects.filter(user_type=0),
                   "STATUSES": Order.STATUS_CHOICES
                   })


def courier(request, user, number):
    """courier handler"""
    if request.method == "POST":
        # validation
        order = Order.objects.get(courier=user, id=int(number))

        if order:
            print(order)
            order.status = int(request.POST.get("update_status"))
            print(order)
            order.save()
        else:
            return error(request, "It isn't your order!")

    if number is None:
        return render(request,
                      "main/courier.html",
                      {"COMPANY": COMPANY,
                       "title": "courier",
                       "orders": Order.objects.filter(courier=user)})

    return render(request, "main/product_page.html", {
        "title": "courier",
        "COMPANY": COMPANY,
        "order": Order.objects.get(courier=user, id=int(number)),
        "STATUSES": Order.STATUS_CHOICES
        # verification is this order belong to this courier

    })


@check_session
@login_required
def show_page(request, user: User, number=None):
    try:
        if user.user_type == 1:
            return manager(request, number)
        elif user.user_type == 0:
            return courier(request, user, number)
        else:
            return error(request, "The administrator assigned you the wrong user type. ")

    except Exception:
        return error(request)


@check_session
def make_order(request, product=None):
    try:
        product_obj = Product.objects.get(tag=product)
        if product is None or product_obj is None:
            redirect("shop_page")

        if request.method == "POST":
            current = Order()
            # print(request.POST)
            current.phone = request.POST.get("phone")
            current.address = request.POST.get("address")
            current.district = check_location(request.POST.get("address"))

            if product_obj.count < int(request.POST.get("count")):
                return error(request, "Sorry, but you choose too much products")
            else:
                product_obj.count -= int(request.POST.get("count"))
                product_obj.save()
                current.save()

        return render(request, "main/make_order.html", {
            "COMPANY": COMPANY,
            "title": "Buy",
            "product": Product.objects.get(tag=product)
        })
    except Exception:
        return error(request)
