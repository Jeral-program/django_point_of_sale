# Generated by Django 4.1.5 on 2024-01-10 06:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_product_author_alter_product_published'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='author',
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default='autor', max_length=256),
        ),
        migrations.AlterField(
            model_name='product',
            name='published',
            field=models.DateField(default=datetime.datetime(2024, 1, 10, 6, 28, 37, 992074, tzinfo=datetime.timezone.utc)),
        ),
    ]
