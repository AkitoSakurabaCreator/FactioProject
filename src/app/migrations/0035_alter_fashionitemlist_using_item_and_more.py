# Generated by Django 4.1.3 on 2023-03-01 06:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0034_alter_fashionsavelist_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fashionitemlist',
            name='using_item',
            field=models.CharField(max_length=20, verbose_name='使用アイテム'),
        ),
        migrations.AlterField(
            model_name='fashionsavelist',
            name='author',
            field=models.IntegerField(verbose_name='作者アカウントID'),
        ),
        migrations.AlterField(
            model_name='fashionsavelist',
            name='brand',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ブランド'),
        ),
        migrations.AlterField(
            model_name='fashionsavelist',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='カテゴリー'),
        ),
        migrations.AlterField(
            model_name='fashionsavelist',
            name='clothing',
            field=models.CharField(default='nothing', max_length=100, verbose_name='ジャンル'),
        ),
        migrations.AlterField(
            model_name='fashionsavelist',
            name='color',
            field=models.CharField(default='', max_length=10, verbose_name='ベースカラー'),
        ),
        migrations.AlterField(
            model_name='fashionsavelist',
            name='description',
            field=models.TextField(verbose_name='説明'),
        ),
        migrations.AlterField(
            model_name='fashionsavelist',
            name='publish',
            field=models.BooleanField(default=False, verbose_name='公開'),
        ),
        migrations.AlterField(
            model_name='fashionsavelist',
            name='season',
            field=models.CharField(default='オールシーズン', max_length=100, verbose_name='季節'),
        ),
        migrations.AlterField(
            model_name='fashionsavelist',
            name='sex',
            field=models.CharField(default='Free', max_length=5, verbose_name='性別'),
        ),
        migrations.AlterField(
            model_name='fashionsavelist',
            name='slug',
            field=models.IntegerField(verbose_name='固有ID'),
        ),
        migrations.AlterField(
            model_name='fashionsavelist',
            name='title',
            field=models.CharField(max_length=100, verbose_name='タイトル'),
        ),
        migrations.AlterField(
            model_name='review',
            name='bought',
            field=models.BooleanField(default=False, verbose_name='購入者'),
        ),
        migrations.CreateModel(
            name='LikeForItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
