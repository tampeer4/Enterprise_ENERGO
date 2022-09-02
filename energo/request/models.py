import email
import pytz  
import datetime
from turtle import title
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

now = datetime.datetime.now()

class Topic(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Тему'
        verbose_name_plural = 'Темы'

class Part(models.Model):
    THEME_CHOICES = (
        ('кг', 'Киллограмм'),
        ('шт', 'Штука'),
        ('г', 'Грамм'),
    )
    pub_date = models.DateTimeField(auto_now = True)
    prod_name = models.CharField(max_length=200)
    full_prod_name = models.CharField(max_length=200)
    topic_work = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE
    )
    count = models.CharField(max_length=10, default=1)
    unit_storage = models.CharField(
        max_length=9,
        choices=THEME_CHOICES,
        default="кг")
    cell_store = models.CharField(max_length=100)
    man = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='name'
    )
    email = models.EmailField(blank=True,null=True)
    def __str__(self):
        return self.prod_name
    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Карточку'
        verbose_name_plural = 'Карточка'


class Request(models.Model):
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        verbose_name=('Тема проекта')
    )
    pub_date = models.DateTimeField(auto_now = True)
    fio = models.CharField(max_length=100, verbose_name=('ФИО'))
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class Request_Part(models.Model):
    THEME_CHOICES = (
        ('ссылка','Ссылка'),
        ('артикул','Артикул'),
        ('фирма','Фирма'),
    )
    THEME_CHOICES_Quantity = (
        ('кг', 'Киллограмм'),
        ('шт', 'Штука'),
        ('г', 'Грамм'),
    )
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    part = models.ForeignKey(
        Part, 
        on_delete=models.CASCADE,
        verbose_name=('Карточка товара'),)
    count = models.IntegerField(default=1, verbose_name=('Количество'))
    unit_storage = models.CharField(
        max_length=9,
        choices=THEME_CHOICES_Quantity,
        default="кг",
        verbose_name=('Единица измерения'))
    link = models.CharField(
        max_length=40,
        choices=THEME_CHOICES,
        default="Ссылка",
        verbose_name=('Ссылка'),
        blank=True,null=True,
        )
    link_url = models.CharField(
        max_length=500,
        verbose_name=('pass'),
        default='',
        blank=True,null=True)
    class Meta:
        verbose_name = 'Заявка на товар'
        verbose_name_plural = 'Заявка на товары'
    