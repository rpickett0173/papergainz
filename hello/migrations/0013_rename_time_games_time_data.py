# Generated by Django 3.2 on 2021-04-30 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0012_alter_dotaplayerranking_rank'),
    ]

    operations = [
        migrations.RenameField(
            model_name='games',
            old_name='time',
            new_name='time_data',
        ),
    ]
