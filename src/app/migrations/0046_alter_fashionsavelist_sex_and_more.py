# Generated by Django 4.1.3 on 2023-03-05 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0045_alter_item_color_alter_item_sex_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fashionsavelist',
            name='sex',
            field=models.CharField(default='自由', max_length=2, verbose_name='性別'),
        ),
        migrations.AlterField(
            model_name='favoritefashionlistitem',
            name='favorite_item',
            field=models.IntegerField(verbose_name='お気に入りファッションコーデ'),
        ),
    ]
