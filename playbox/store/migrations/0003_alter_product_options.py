# Generated by Django 5.0.6 on 2024-06-22 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-created_at',)},
        ),
    ]
