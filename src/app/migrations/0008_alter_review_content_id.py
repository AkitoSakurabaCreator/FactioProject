# Generated by Django 4.1.3 on 2023-02-18 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_review_content_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='content_id',
            field=models.SlugField(),
        ),
    ]