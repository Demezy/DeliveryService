from django.db import models
import random
from hashlib import sha256

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'


def key_gen():
    password = ''

    for i in range(10):
        password += random.choice(chars)

    return password


class User(models.Model):
    id = models.AutoField('id', primary_key=True, auto_created=True)
    username = models.CharField('username', max_length=100, unique=True)
    email = models.CharField('email', max_length=100, blank=True)
    password = models.TextField('password', blank=True)
    invitation_code = models.TextField('invitation_code', default=key_gen)

    def __str__(self):
        return f'Name: {self.username}{" " * 4}Email:{self.email}{" " * 4}UserType:{self.invitation_code}'
