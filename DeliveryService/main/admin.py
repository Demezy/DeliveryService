from django.contrib import admin
from .models import Courier, Product, Manager, Order

admin.site.register(Courier)
admin.site.register(Manager)
admin.site.register(Order)
admin.site.register(Product)
