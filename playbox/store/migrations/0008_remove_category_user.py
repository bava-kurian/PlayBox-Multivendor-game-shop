# Generated by Django 5.0.6 on 2024-06-23 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='user',
        ),
    ]
