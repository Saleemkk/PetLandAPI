# Generated by Django 4.0.4 on 2022-05-04 15:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character_id', models.UUIDField(default=uuid.uuid4)),
                ('gender', models.CharField(max_length=10000)),
                ('hair_id', models.UUIDField(default=uuid.uuid4)),
                ('hair_color', models.UUIDField(default=uuid.uuid4)),
                ('eye_id', models.UUIDField(default=uuid.uuid4)),
                ('eyebrow_id', models.UUIDField(default=uuid.uuid4)),
                ('eyebrow_color', models.CharField(max_length=10000)),
                ('nose_id', models.CharField(max_length=10000)),
                ('mouth_id', models.UUIDField(default=uuid.uuid4)),
                ('beard_id', models.UUIDField(default=uuid.uuid4)),
                ('beard_color', models.CharField(max_length=10000)),
                ('clothing_id', models.UUIDField(default=uuid.uuid4)),
                ('pants_id', models.UUIDField(default=uuid.uuid4)),
                ('shoes_id', models.UUIDField(default=uuid.uuid4)),
            ],
        ),
    ]
