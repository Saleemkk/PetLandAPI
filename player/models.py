import uuid
from django.db import models


class Player(models.Model):
    wallet_address = models.TextField(null=True, blank=True, unique=True)
    user_name = models.CharField(max_length=100, blank=True,null=True)
    gender = models.CharField(max_length=100)
    hair_style = models.CharField(max_length=100, blank=True,null=True)
    hair_color = models.CharField(max_length=100, blank=True,null=True)
    eye = models.CharField(max_length=100,blank=True, null=True)
    eyebrow_style = models.CharField(max_length=100, blank=True,null=True)
    eyebrow_color = models.CharField(max_length=100, blank=True,null=True)
    nose = models.CharField(max_length=100, blank=True,null=True)
    mouth = models.CharField(max_length=100, blank=True,null=True)
    beard_style = models.CharField(max_length=100, blank=True,null=True)
    beard_color = models.CharField(max_length=100, blank=True,null=True)
    shirt = models.CharField(max_length=100, blank=True,null=True)
    pants = models.CharField(max_length=100, blank=True,null=True)
    shoes_style = models.CharField(max_length=100, blank=True,null=True)
    body_color = models.CharField(max_length=100, null=True, blank=True)
    white_check_mark = models.BooleanField(default=False, blank=True,null=True)
    raised_hands = models.BooleanField(default=False, blank=True,null=True)

    def __str__(self):
        return self.first_name




class Pet(models.Model):
    nft_id = models.TextField(null=True, blank=True, unique=True)
    nft_image=models.ImageField('images/')

    pet_name = models.CharField(max_length=100, null=True)
    breed = models.IntegerField()
    pet_color = models.CharField(max_length=100, null=True)


    # traits = 

    #  traits = ArrayField(
    #     ArrayField(
    #         models.CharField(max_length=10, blank=True),
    #         size=8,
    #     ),
    #     size=8,
    # )

    
    # traits_value=

    phase = models.IntegerField()

    level = models.IntegerField()

    exp = models.IntegerField()


    def __str__(self):
        return self.pet_name




class Land(models.Model):
    landnft_id = models.TextField(null=True, blank=True, unique=True)
    landnft_image=models.ImageField('images/')

    land_name = models.CharField(max_length=100, null=True)
    size = models.IntegerField()

