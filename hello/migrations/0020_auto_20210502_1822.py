# Generated by Django 3.2 on 2021-05-02 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0019_auto_20210502_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bets',
            name='bet_odds',
            field=models.DecimalField(decimal_places=2, default=1.5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='games',
            name='team1_amount',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='games',
            name='team2_amount',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
