# Generated by Django 4.0.4 on 2022-05-12 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0004_player_body_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='eyes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='raised_hands',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='wallet_address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='white_check_mark',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]