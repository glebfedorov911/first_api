# Generated by Django 5.0 on 2023-12-18 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kisy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promo',
            name='promo',
            field=models.TextField(default='kisypromo6291907', max_length=100, unique=True),
        ),
    ]
