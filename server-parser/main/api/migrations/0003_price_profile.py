# Generated by Django 2.2.3 on 2019-07-11 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190711_0756'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_price', models.PositiveIntegerField(blank=True, null=True, verbose_name='Цена от')),
                ('to_price', models.IntegerField(blank=True, null=True, verbose_name='Цена до')),
            ],
            options={
                'verbose_name': 'Цена',
                'verbose_name_plural': 'Цены',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ссылка')),
                ('active', models.BooleanField(blank=True, default=True, null=True, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
    ]