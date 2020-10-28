from django.db import models
from random import choice


# from hashlib import sha256


class User(models.Model):
    id = models.AutoField('id', primary_key=True, auto_created=True)
    username = models.CharField('username', max_length=100, unique=True)
    password = models.TextField('password')
    district = models.PositiveIntegerField("district", null=True, default=None, blank=True)
    USER_TYPES = (
        (0, "Courier"),
        (1, "Manager"),
    )
    user_type = models.PositiveIntegerField("type", default=0, choices=USER_TYPES)

    def __str__(self):
        return f"{self.username} district: {self.district}"


class Order(models.Model):
    id = models.AutoField('id', primary_key=True, auto_created=True)
    phone = models.CharField("phone", blank=False, max_length=12)
    address = models.CharField('address', max_length=100, blank=False)
    district = models.PositiveIntegerField("district", default=0)  # 0 is some unusual district
    courier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    STATUS_CHOICES = (
        (-1, "order canceled"),
        (0, "processing"),
        (1, "took order"),
        (2, "delivering"),
        (3, "finish"),
        (4, "lose"),
    )
    status = models.IntegerField("status", choices=STATUS_CHOICES, blank=False, default=0)

    def __str__(self):
        return f"status: {self.status}, address: {self.district}-{self.address}, phone: {self.phone}"


class Product(models.Model):
    id = models.AutoField('id', primary_key=True, auto_created=True)
    title = models.CharField("title", max_length=100)
    text = models.TextField("text", max_length=300, blank=True)
    count = models.PositiveIntegerField(default=0)
    img = models.CharField("img", max_length=100, blank=True)
    price = models.PositiveIntegerField("price", default=0)
    tag = models.CharField("tag", max_length=100, unique=True, default="")

    def __str__(self):
        return f"{self.title}\t-- price: {self.price}, count: {self.count}"
