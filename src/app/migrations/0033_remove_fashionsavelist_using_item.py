# Generated by Django 4.1.3 on 2023-02-24 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_alter_fashionsavelist_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fashionsavelist',
            name='using_item',
        ),
    ]