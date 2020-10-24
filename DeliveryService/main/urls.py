from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("test", views.test_page, name="test_page"),
    path("Shop", views.shop_page, name="shop_page"),
    path("manager", views.manage_page, name="manage_page")
]

