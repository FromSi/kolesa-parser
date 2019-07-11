# Generated by Django 2.2.3 on 2019-07-11 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('value', models.CharField(blank=True, max_length=255, null=True, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('value', models.CharField(blank=True, max_length=255, null=True, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Марка машины',
                'verbose_name_plural': 'Марки машин',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('value', models.CharField(blank=True, max_length=255, null=True, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Тип машины',
                'verbose_name_plural': 'Типы машины',
            },
        ),
    ]