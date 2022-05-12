import uuid
from django.db import models


class Player(models.Model):
    wallet_address = models.TextField(null=True, blank=True, unique=True)
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
    body_color = models.CharField(max_length=10000, null=True, blank=True)
    white_check_mark = models.BooleanField(default=False, null=True, blank=True)
    eyes = models.TextField(null=True, blank=True)
    raised_hands = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.first_name
