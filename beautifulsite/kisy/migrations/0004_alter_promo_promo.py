# Generated by Django 5.0 on 2023-12-18 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kisy', '0003_alter_promo_promo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promo',
            name='promo',
            field=models.TextField(default='kisypromo1261202', max_length=100, unique=True),
        ),
    ]
