# Generated by Django 5.0 on 2023-12-18 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kisy', '0008_alter_user_unique_together_user_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promo',
            name='promo',
            field=models.TextField(default='kisypromo612816', max_length=100, unique=True),
        ),
    ]