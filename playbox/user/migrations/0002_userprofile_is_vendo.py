# Generated by Django 4.2.5 on 2024-06-26 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_vendo',
            field=models.BooleanField(default=False),
        ),
    ]