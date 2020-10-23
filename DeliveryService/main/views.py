from django.shortcuts import render
from .models import User

# constants
COMPANY = "Delivery Service"


# from django.http import HttpResponse
# todo replace TEMP to DB
class TEMP:
    """temporary class for test"""

    def __init__(self, num: str) -> None:
        self.title = "TestTitle" + num
        self.text = "Text" + num
        self.count = num
        self.img = "super.png"

    def __str__(self):
        return "STRING"


products = [TEMP(str(i)) for i in range(10)]


def index(request):
    # return HttpResponse("<h1> Index page </h1>")
    # data = User.objects.get(id=1) # example
    return render(request, "main/index.html", {"title": "Home"})


def test_page(request):
    return render(request, "main/test.html", {"products": products, "COMPANY": COMPANY})
