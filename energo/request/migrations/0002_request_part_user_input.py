# Generated by Django 2.2.19 on 2022-09-05 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='request_part',
            name='user_input',
            field=models.CharField(default='', max_length=500, verbose_name='Пользовательский ввод'),
        ),
    ]
