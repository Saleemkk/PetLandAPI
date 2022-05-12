from rest_framework import serializers
from .models import Player

class PlayerSerializer(serializers.ModelSerializer):
    
    character_id = serializers.ReadOnlyField()
    hair_id = serializers.ReadOnlyField()
    eye_id = serializers.ReadOnlyField()
    eyebrow_id = serializers.ReadOnlyField()
    nose_id = serializers.ReadOnlyField()
    mouth_id = serializers.ReadOnlyField()
    beard_id = serializers.ReadOnlyField()
    clothing_id = serializers.ReadOnlyField()
    pants_id = serializers.ReadOnlyField()
    shoes_id = serializers.ReadOnlyField()

    class Meta:
        model = Player
        fields = "__all__"