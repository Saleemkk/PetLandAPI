import uuid
from django.db import models


class Player(models.Model):
    first_name = models.CharField(max_length=10000, null=True)
    last_name = models.CharField(max_length=10000, null=True)
    character_id = models.UUIDField(default = uuid.uuid4)
    gender = models.CharField(max_length=10000)
    hair_id = models.UUIDField(default = uuid.uuid4)
    hair_color = models.CharField(max_length=10000, null=True)
    eye_id = models.UUIDField(default = uuid.uuid4)
    eyebrow_id = models.UUIDField(default = uuid.uuid4)
    eyebrow_color = models.CharField(max_length=10000)
    nose_id = models.UUIDField(default = uuid.uuid4)
    mouth_id = models.UUIDField(default = uuid.uuid4)
    beard_id = models.UUIDField(default = uuid.uuid4)
    beard_color = models.CharField(max_length=10000)
    clothing_id = models.UUIDField(default = uuid.uuid4)
    pants_id = models.UUIDField(default = uuid.uuid4)
    shoes_id = models.UUIDField(default = uuid.uuid4)

    def __str__(self):
        return self.first_name
