# Generated by Django 3.2 on 2021-05-02 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0017_auto_20210501_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='balance',
            field=models.PositiveIntegerField(default=10000),
        ),
    ]