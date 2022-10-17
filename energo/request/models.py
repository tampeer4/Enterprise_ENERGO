import email
from pyexpat import model
import pytz  
import datetime
from turtle import title
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

now = datetime.datetime.now()

class Topic(models.Model):
    title = models.CharField(max_length=200,verbose_name=('Тема'))
    description = models.TextField(verbose_name=('Описание'))
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
    pub_date = models.DateTimeField(auto_now = True,verbose_name=('Дата'))
    prod_name = models.CharField(max_length=200,verbose_name=('Наименование'))
    full_prod_name = models.CharField(max_length=200, verbose_name=('Полное наименование'))
    topic_work = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        verbose_name=('Тема проекта')
    )
    count = models.IntegerField(default=1, verbose_name=('Количество'))
    unit_storage = models.CharField(
        max_length=9,
        choices=THEME_CHOICES,
        default="кг",
        verbose_name=('Эквивалент')
        )
    cell_store = models.CharField(
        max_length=100,
        blank=True,null=True,
        verbose_name=('Место нахождения'),
    )
    man = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=('Имя пользователя'),
    )
    def __str__(self):
        return self.prod_name
    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Наименование ПКИ'
        verbose_name_plural = 'Наименование ПКИ'


class Request_Man(models.Model):
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        verbose_name=('Тема проекта')
    )
    pub_date = models.DateTimeField(auto_now = True, verbose_name=('Дата'))
    fio = models.CharField(max_length=100, verbose_name=('ФИО'))
    email = models.EmailField(blank=True,null=True,)
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
    request = models.ForeignKey(Request_Man, on_delete=models.CASCADE,)
    part = models.ForeignKey(
        Part, 
        on_delete=models.CASCADE,
        verbose_name=('Наименование ПКИ'),
        blank=True,null=True,
        )
    user_input = models.CharField(
        max_length=500,
        verbose_name=('Пользовательский ввод'),
        default='',
        blank=True,null=True,
        help_text = 'Пишите сюда, если не нашли подходящий вариант в "Наименование ПКИ"'
        )
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

class Write_Off(models.Model):
    THEME_CHOICES = (
        ('кг', 'Киллограмм'),
        ('шт', 'Штука'),
        ('г', 'Грамм'),
    )
    fio = models.CharField(max_length=100, verbose_name=('ФИО'))
    pub_date = models.DateTimeField(auto_now = True, verbose_name=('Дата'))
    part = models.ForeignKey(
        Part, 
        on_delete=models.CASCADE,
        verbose_name=('Наименование ПКИ'),
        blank=True,null=True,
    )
    count = models.IntegerField()
    unit_storage = models.CharField(
        max_length=9,
        choices=THEME_CHOICES,
        default="кг",
        verbose_name=('Эквивалент')
        )
    class Meta:
        verbose_name = 'Списание товара'
        verbose_name_plural = 'Списание товаров'
