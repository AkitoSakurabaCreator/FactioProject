# Generated by Django 4.1.3 on 2023-02-22 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_customuser_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='year',
            field=models.DateTimeField(auto_now=True, max_length=20, verbose_name='生年月日'),
        ),
    ]
