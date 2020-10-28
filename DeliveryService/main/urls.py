from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("test", views.test_page, name="test_page"),
    path("test/<num>", views.test_page, name="test_page"),
    path("Shop", views.shop_page, name="shop_page"),
    path("manager/<number>", views.show_page, name="manage_page"),
    path("manager", views.show_page, name="manage_page"),
    path("courier", views.show_page, name="courier"),
    path("courier/<number>", views.show_page, name="courier"),
    path("login", views.login, name="login"),
    path("error", views.error, name="error"),
    path("logout", views.logout, name="logout")
]
