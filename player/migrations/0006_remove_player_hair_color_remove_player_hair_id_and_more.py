# Generated by Django 4.0.4 on 2022-05-14 18:18

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0005_player_eyes_player_raised_hands_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='hair_color',
        ),
        migrations.RemoveField(
            model_name='player',
            name='hair_id',
        ),
        migrations.AlterField(
            model_name='player',
            name='wallet_address',
            field=models.TextField(blank=True, null=True, unique=True),
        ),
        migrations.CreateModel(
            name='HairModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hair_color', models.CharField(max_length=10000)),
                ('hair_id', models.UUIDField(default=uuid.uuid4)),
                ('player', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='player.player')),
            ],
        ),
    ]
