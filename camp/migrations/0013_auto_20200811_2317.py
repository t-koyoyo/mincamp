# Generated by Django 2.0 on 2020-08-11 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0012_auto_20200811_2311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation_Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='タイトル')),
                ('detail', models.CharField(max_length=200, verbose_name='内容')),
                ('is_anonymous', models.BooleanField(default=False, verbose_name='匿名フラグ')),
                ('rank', models.IntegerField(verbose_name='レビューランク')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
            ],
            options={
                'verbose_name_plural': '予約レビュー',
            },
        ),
        migrations.AlterModelOptions(
            name='reservation',
            options={'verbose_name_plural': '予約'},
        ),
        migrations.AddField(
            model_name='reservation_review',
            name='reservation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='camp.Reservation', verbose_name='予約外部キー'),
        ),
    ]
