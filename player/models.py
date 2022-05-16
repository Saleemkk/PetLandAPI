import uuid
from django.db import models


class Player(models.Model):
    wallet_address = models.TextField(null=True, blank=True, unique=True)
    first_name = models.CharField(max_length=10000, null=True)
    last_name = models.CharField(max_length=10000, null=True)
    character_id = models.UUIDField(default = uuid.uuid4)
    gender = models.CharField(max_length=10000)
    # hair_id = models.UUIDField(default = uuid.uuid4)
    # hair_color = models.CharField(max_length=10000, null=True)
    # eye_id = models.UUIDField(default = uuid.uuid4)
    # eyebrow_id = models.UUIDField(default = uuid.uuid4)
    # eyebrow_color = models.CharField(max_length=10000)
    # nose_id = models.UUIDField(default = uuid.uuid4)
    # mouth_id = models.UUIDField(default = uuid.uuid4)
    # beard_id = models.UUIDField(default = uuid.uuid4)
    # beard_color = models.CharField(max_length=10000)
    # clothing_id = models.UUIDField(default = uuid.uuid4)
    # pants_id = models.UUIDField(default = uuid.uuid4)
    # shoes_id = models.UUIDField(default = uuid.uuid4)
    # body_color = models.CharField(max_length=10000, null=True, blank=True)
    white_check_mark = models.BooleanField(default=False, null=True, blank=True)
    eyes = models.TextField(null=True, blank=True)
    raised_hands = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.first_name


class HairModel(models.Model):
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name="hair_id"
    )
    # hair_color = models.CharField(max_length=10000)
    hair_id = models.UUIDField(default = uuid.uuid4)

    def __str__(self):
        return self.hair_id



class HairColorModel(models.Model):
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name="hair_color"
    )
    hair_color = models.CharField(max_length=10000)
    # hair_id = models.UUIDField(default = uuid.uuid4)

    def __str__(self):
        return self.hair_color



class EyeModel(models.Model):
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name="eye_id"
    )
    eye_id = models.UUIDField(default = uuid.uuid4)

    def __str__(self):
        return self.eye_id



class EyeBrowModel(models.Model):
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name="eyebrow_id"
    )
    # eyebrow_color = models.CharField(max_length=10000)
    eyebrow_id = models.UUIDField(default = uuid.uuid4)

    def __str__(self):
        return self.eyebrow_id


class EyeBrowColorModel(models.Model):
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name="eyebrow_color"
    )
    eyebrow_color = models.CharField(max_length=10000)
    #] eyebrow_id = models.UUIDField(default = uuid.uuid4)

    def __str__(self):
        return self.eyebrow_color

class NoseModel(models.Model):
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name="nose_id"
    )
    nose_id = models.UUIDField(default = uuid.uuid4)

    def __str__(self):
        return self.nose_id


class MouthModel(models.Model):
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name="mouth_id"
    )
    mouth_id = models.UUIDField(default = uuid.uuid4)

    def __str__(self):
        return self.mouth_id


class BeardModel(models.Model):
    player = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name="beard_id"
    )
    # beard_color = models.CharField(max_length=10000)
    beard_id = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.beard_id;

class BeardColorModel(models.Model):
    player = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name="beard_color"
    )
    beard_color = models.CharField(max_length=10000)
    # beard_id = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.beard_color;


class ClothingModel(models.Model):
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name="clothing_id"
    )
    clothing_id = models.UUIDField(default = uuid.uuid4)

    def __str__(self):
        return self.clothing_id



    
class PantsModel(models.Model):
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name="pants_id"
    )
    pants_id = models.UUIDField(default = uuid.uuid4)

    def __str__(self):
        return self.pants_id


class ShoesModel(models.Model):
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name="shoes_id"
    )
    shoes_id = models.UUIDField(default = uuid.uuid4)

    def __str__(self):
        return self.shoes_id


class BodyColorModel(models.Model):
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name="body_color"
    )
    body_color = models.CharField(max_length=10000, null=True, blank=True)

    def __str__(self):
        return self.eye_id

    
