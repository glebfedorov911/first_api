# Generated by Django 5.0 on 2023-12-19 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kisy', '0022_alter_promo_promo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
