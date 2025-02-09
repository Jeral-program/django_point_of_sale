# Generated by Django 4.1.5 on 2024-01-10 12:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_remove_product_author_alter_product_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=256),
        ),
        migrations.AlterField(
            model_name='product',
            name='published',
            field=models.DateField(default=datetime.datetime(2024, 1, 10, 12, 32, 39, 405936, tzinfo=datetime.timezone.utc)),
        ),
    ]
