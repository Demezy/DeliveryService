from django.db import models
from random import choice

# from hashlib import sha256

# these symbols are used to generate passwords
CHARS = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'


def pass_gen() -> str:
    return "".join([choice(CHARS) for i in range(10)])


class Courier(models.Model):
    id = models.AutoField('id', primary_key=True, auto_created=True)
    username = models.CharField('username', max_length=100, unique=True)
    password = models.TextField('password', default=pass_gen)
    district = models.IntegerField("district", default=0)  # 0 is any district
    invitation_code = models.TextField('invitation_code', default=pass_gen)

    # rating = models.IntegerField("rating", default=0)  # TODO: rating system

    def __str__(self):
        return f"name: {self.username}, district: {self.district}"


class Manager(models.Model):
    id = models.AutoField('id', primary_key=True, auto_created=True)
    username = models.CharField('username', max_length=100, unique=True)
    password = models.TextField('password', default=pass_gen)

    def __str__(self):
        return f"{self.username}(manager)"


class Order(models.Model):
    id = models.AutoField('id', primary_key=True, auto_created=True)
    phone = models.CharField("phone", blank=False, max_length=12)
    address = models.CharField('address', max_length=100, blank=False)
    district = models.IntegerField("district", default=0)  # 0 is some unusual district
    courier = models.ForeignKey(Courier, on_delete=models.SET_DEFAULT, default="", blank=True)
    STATUS_CHOICES = (
        (-1, "order canceled"),
        (1, "took order"),
        (2, "delivering"),
        (3, "finish"),
        (4, "lose"),
    )
    status = models.IntegerField("status", choices=STATUS_CHOICES, blank=False)

    def __str__(self):
        return f"status: {self.status}, address: {self.district}-{self.address}, phone: {self.phone}"


class Product(models.Model):
    id = models.AutoField('id', primary_key=True, auto_created=True)
    title = models.CharField("title", max_length=100, blank=True, unique=True)
    text = models.TextField("text", max_length=300, blank=True)
    count = models.IntegerField(default=0)
    img = models.CharField("img", max_length=100, blank=True)

    # TODO: validation for empty img

    def __str__(self):
        return f"{self.title}\t -- {self.count}"
