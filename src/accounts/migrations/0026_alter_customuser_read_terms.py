# Generated by Django 4.1.3 on 2023-03-05 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_customuser_read_terms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='read_terms',
            field=models.BooleanField(default=False, verbose_name='利用規約同意'),
        ),
    ]
