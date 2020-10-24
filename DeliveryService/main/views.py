from django.shortcuts import render
from .models import User, Product

# constants
COMPANY = "Delivery Service"


def index(request):
    # return HttpResponse("<h1> Index page </h1>")
    # data = User.objects.get(id=1) # example
    return render(request, "main/index.html", {"products": Product.objects.all(), "COMPANY": COMPANY})


def test_page(request):
    return render(request, "main/test.html", {"products": Product.objects.all(), "COMPANY": COMPANY})
