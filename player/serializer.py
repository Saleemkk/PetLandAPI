from rest_framework import serializers
from .models import Land, Pet, Player

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"




class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = "__all__"



class LandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Land
        fields = "__all__"

