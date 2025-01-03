# Generated by Django 4.1.3 on 2023-02-23 11:24

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_alter_customuser_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_screen_id',
            field=models.SlugField(default=accounts.models.create_id, max_length=30, unique=True, verbose_name='ユーザーID'),
        ),
    ]
