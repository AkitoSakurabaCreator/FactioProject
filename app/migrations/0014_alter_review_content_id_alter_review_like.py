# Generated by Django 4.1.3 on 2023-02-20 05:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_review_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='content_id',
            field=models.SlugField(verbose_name='アイテムID'),
        ),
        migrations.AlterField(
            model_name='review',
            name='like',
            field=models.IntegerField(default=3, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='評価'),
        ),
    ]
