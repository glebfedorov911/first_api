# Generated by Django 5.0 on 2023-12-19 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kisy', '0020_user_username_alter_promo_promo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promo',
            name='discount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='promo',
            name='promo',
            field=models.TextField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
