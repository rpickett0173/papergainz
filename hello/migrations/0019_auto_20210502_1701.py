# Generated by Django 3.2 on 2021-05-02 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0018_alter_users_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='bets',
            name='bet_odds',
            field=models.DecimalField(decimal_places=2, default=1.5, max_digits=3),
        ),
        migrations.AlterField(
            model_name='games',
            name='team1_odds',
            field=models.DecimalField(decimal_places=2, default=1.5, max_digits=3),
        ),
        migrations.AlterField(
            model_name='games',
            name='team2_odds',
            field=models.DecimalField(decimal_places=2, default=1.5, max_digits=3),
        ),
    ]
