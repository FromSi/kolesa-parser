# Generated by Django 2.2.3 on 2019-07-12 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_remove_ad_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ad',
            field=models.ManyToManyField(blank=True, null=True, to='api.Ad', verbose_name='Объявления'),
        ),
    ]