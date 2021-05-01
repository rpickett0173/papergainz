# Generated by Django 3.2 on 2021-04-29 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0008_auto_20210429_1212'),
    ]

    operations = [
        migrations.CreateModel(
            name='DotaPlayerRanking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('rank', models.PositiveIntegerField()),
                ('avatar', models.TextField(blank=True)),
            ],
        ),
    ]
