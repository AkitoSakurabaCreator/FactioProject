# Generated by Django 4.1.3 on 2023-02-22 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_customuser_user_screen_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='year',
            field=models.DateTimeField(blank=True, max_length=20, verbose_name='生年月日'),
        ),
    ]
