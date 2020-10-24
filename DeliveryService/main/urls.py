from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("test", views.test_page, name="test_page"),
]
