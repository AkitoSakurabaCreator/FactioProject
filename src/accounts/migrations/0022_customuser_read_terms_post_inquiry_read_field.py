# Generated by Django 4.1.3 on 2023-03-05 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_alter_customuser_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='read_terms',
            field=models.BooleanField(default=False, verbose_name='利用規約同意'),
        ),
        migrations.AddField(
            model_name='post_inquiry',
            name='read_field',
            field=models.BooleanField(default=False, verbose_name='お問い合わせ送信確認'),
        ),
    ]