# Generated by Django 3.2.4 on 2021-06-12 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0009_photoview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='slug',
        ),
    ]
