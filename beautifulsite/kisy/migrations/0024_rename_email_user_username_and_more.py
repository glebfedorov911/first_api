# Generated by Django 5.0 on 2023-12-19 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kisy', '0023_remove_user_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email',
            new_name='username',
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together={('username', 'phone')},
        ),
    ]