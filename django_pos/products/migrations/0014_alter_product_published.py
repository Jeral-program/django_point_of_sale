# Generated by Django 4.1.5 on 2024-01-13 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_alter_product_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='published',
            field=models.CharField(max_length=256),
        ),
    ]
