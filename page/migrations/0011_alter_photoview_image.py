# Generated by Django 3.2.4 on 2021-06-12 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0010_remove_order_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photoview',
            name='image',
            field=models.ImageField(blank=True, upload_to='photos'),
        ),
    ]
