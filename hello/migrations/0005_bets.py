# Generated by Django 3.2 on 2021-04-22 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0004_rewards'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_ID', models.PositiveIntegerField()),
                ('game_ID', models.PositiveIntegerField()),
                ('date_placed', models.DateTimeField(auto_now=True)),
                ('bet_amount', models.PositiveIntegerField()),
                ('win', models.BooleanField()),
            ],
        ),
    ]