# Generated by Django 4.1.3 on 2023-02-21 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_item_color_alter_item_brand_alter_item_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to='products_images', verbose_name='イメージ画像'),
        ),
    ]
