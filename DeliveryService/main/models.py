from django.db import models
import random
from hashlib import sha256

# these symbols are used to generate passwords
CHARS = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'


# TODO: rename keygen to pass_gen
def pass_gen() -> str:
    return "".join([random.choice(CHARS) for i in range(10)])


class User(models.Model):
    id = models.AutoField('id', primary_key=True, auto_created=True)
    username = models.CharField('username', max_length=100, unique=True)
    email = models.CharField('email', max_length=100, blank=True)
    password = models.TextField('password', blank=True)
    invitation_code = models.TextField('invitation_code', default=pass_gen)

    def __str__(self):
        return f'Name: {self.username}{" " * 4}Email:{self.email}{" " * 4}UserType:{self.invitation_code}'


class Product(models.Model):
    id = models.AutoField('id', primary_key=True, auto_created=True)
    title = models.CharField("title", max_length=100, blank=True, unique=True)
    text = models.TextField("text", max_length=300, blank=True)
    count = models.IntegerField(null=False, default=0)
    img = models.CharField("img", max_length=100, blank=True)

    # TODO: validation for empty img

    def __str__(self):
        return f"{self.title}\t -- {self.count}"
