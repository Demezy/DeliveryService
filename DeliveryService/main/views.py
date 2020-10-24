from django.shortcuts import render
from .models import User, Product

# constants
COMPANY = "Delivery Service"


def index(request):
    # return HttpResponse("<h1> Index page </h1>")
    # data = User.objects.get(id=1) # example
    return render(request, "main/index.html", {"title": "LinkPage", "COMPANY": COMPANY})
    # return render(request, "main/index.html", {"products": Product.objects.all(), "COMPANY": COMPANY})


def shop_page(request):
    return render(request, "main/Shop.html", {"title": "Shop", "products": Product.objects.all(), "COMPANY": COMPANY})


def test_page(request):
    return render(request, "main/test.html",
                  {"title": "TEST PAGE!", "products": Product.objects.all(), "COMPANY": COMPANY})


def manage_page(request):
    return render(request, "main/manage_page.html", {"COMPANY": COMPANY})
