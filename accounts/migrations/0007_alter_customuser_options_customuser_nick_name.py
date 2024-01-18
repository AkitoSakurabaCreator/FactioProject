# Generated by Django 4.1.3 on 2023-02-22 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_customuser_job'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'ユーザー', 'verbose_name_plural': 'ユーザー'},
        ),
        migrations.AddField(
            model_name='customuser',
            name='nick_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='ニックネーム'),
        ),
    ]