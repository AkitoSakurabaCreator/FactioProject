# Generated by Django 4.1.3 on 2023-03-05 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0047_coupon'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='discount',
            field=models.IntegerField(default=0, verbose_name='割引'),
        ),
    ]
