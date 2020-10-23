from django.shortcuts import render
# from django.http import HttpResponse


def index(request):
    # return HttpResponse("<h1> Index page </h1>")
    return render(request, "main/index.html", {"title": "Home"})


def test_page(request):
    return render(request, "main/test.html")
