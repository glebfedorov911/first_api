# Generated by Django 5.0 on 2023-12-18 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kisy', '0005_alter_promo_promo_alter_user_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promo',
            name='promo',
            field=models.TextField(default='kisypromo197602', max_length=100, unique=True),
        ),
    ]
