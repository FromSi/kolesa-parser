# Generated by Django 2.2.3 on 2019-07-11 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='active',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Статус'),
        ),
    ]
