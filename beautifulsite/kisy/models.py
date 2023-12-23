from django.db import models

import random

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import PermissionsMixin

from .managers import UserManager
from django.conf import settings

class User(AbstractBaseUser, PermissionsMixin):
    firstname = models.CharField(max_length=255, blank=True, null=True)
    surname = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=60, blank=False, null=False, unique=True)
    email = models.EmailField(blank=False, null=False, unique=True)
    inst = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    index = models.CharField(max_length=255, blank=True, null=True)
    data_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']

    def __str__(self):
        return f'{self.pk}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        unique_together = ('email', 'phone')

class Goods(models.Model):
    name = models.CharField(max_length=500, blank=False, null=False)
    desc = models.TextField(blank=False, null=False)
    application = models.TextField(blank=True, null=True) # применение
    cost = models.IntegerField(blank=False, null=False)
    image = models.FileField(upload_to='goods/%Y/%m/%d/', blank=True, null=False)
    volume = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.cost}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class Feedback(models.Model):
    goods = models.ForeignKey('Goods', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f'{self.pk} - {self.user.email}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

class Rating(models.Model):
    ONE = '1'
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'

    SCORE = (
        (ONE, '1'),
        (TWO, '2'),
        (THREE, '3'),
        (FOUR, '4'),
        (FIVE, '5'),
    )

    good = models.ForeignKey('Goods', on_delete=models.CASCADE)
    rate = models.CharField(max_length=1, choices=SCORE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.good.pk} - {self.rate}'

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинг'

class Promo(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    promo = models.CharField(max_length=100, unique=True, blank=True, null=True)
    discount = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.promo} - {self.discount}'

    def generate_promo(self):
        proms = Promo.objects.all()
        self.promo = f'kisypromo{len(proms)+1}'
    def save(self, *args, **kwargs):
        self.generate_promo()
        super(Promo, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Промо'
        verbose_name_plural = 'Промо'

class Meditation(models.Model):
    goods = models.ForeignKey('Goods', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='meditation/%Y/%m/%d/')
    audio = models.FileField(blank=True, null=True)

    class Meta:
        verbose_name = 'Медитация'
        verbose_name_plural = 'Медитации'

class Basket(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    goods = models.ForeignKey('Goods', on_delete=models.CASCADE)
    count = models.IntegerField()

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

class Prize(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='prize/%Y/%m/%d/')

    class Meta:
        verbose_name = 'Приз'
        verbose_name_plural = 'Призы'

class Order(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    address = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
