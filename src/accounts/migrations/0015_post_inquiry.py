# Generated by Django 4.1.3 on 2023-02-28 08:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_alter_customuser_user_screen_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post_Inquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='メールアドレス')),
                ('first_name', models.CharField(max_length=30, verbose_name='姓')),
                ('last_name', models.CharField(max_length=30, verbose_name='名')),
                ('title', models.CharField(max_length=100, verbose_name='件名')),
                ('summary', models.TextField(verbose_name='お問い合わせ内容')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='お問い合わせ日')),
            ],
            options={
                'verbose_name': 'お問い合わせ一覧',
                'verbose_name_plural': 'お問い合わせ一覧',
            },
        ),
    ]