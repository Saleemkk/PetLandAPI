from rest_framework import serializers
from .models import BeardColorModel, BeardModel, BodyColorModel, ClothingModel, EyeBrowColorModel, EyeBrowModel, EyeModel, HairColorModel, MouthModel, NoseModel, PantsModel, Player, HairModel, ShoesModel


class HairSerializer(serializers.ModelSerializer):

    hair_id = serializers.ReadOnlyField()

    player = serializers.SlugRelatedField(
        queryset=Player.objects.all(), slug_field='first_name'
    )
    class Meta:
        model = HairModel
        fields = "__all__"

class HairColorSerializer(serializers.ModelSerializer):
	
    player = serializers.SlugRelatedField(
        queryset=Player.objects.all(), slug_field='first_name'
    )
    class Meta:
        model = HairColorModel
        fields = "__all__"


class EyeSerializer(serializers.ModelSerializer):
	
    eye_id = serializers.ReadOnlyField()

    player = serializers.SlugRelatedField(
        queryset=Player.objects.all(), slug_field='first_name'
    )
    class Meta:
        model = EyeModel
        fields = "__all__"


class EyeBrowSerializer(serializers.ModelSerializer):
	
    eyebrow_id = serializers.ReadOnlyField()

    player = serializers.SlugRelatedField(
        queryset=Player.objects.all(), slug_field='first_name'
    )
    class Meta:
        model = EyeBrowModel
        fields = "__all__"

class EyeBrowColorSerializer(serializers.ModelSerializer):
	
    player = serializers.SlugRelatedField(
        queryset=Player.objects.all(), slug_field='first_name'
    )
    class Meta:
        model = EyeBrowColorModel
        fields = "__all__"


class NoseSerializer(serializers.ModelSerializer):
	
    nose_id = serializers.ReadOnlyField()

    player = serializers.SlugRelatedField(
        queryset=Player.objects.all(), slug_field='first_name'
    )
    class Meta:
        model = NoseModel
        fields = "__all__"


class MouthSerializer(serializers.ModelSerializer):
	
    mouth_id = serializers.ReadOnlyField()

    player = serializers.SlugRelatedField(
        queryset=Player.objects.all(), slug_field='first_name'
    )
    class Meta:
        model = MouthModel
        fields = "__all__"


class BeardSerializer(serializers.ModelSerializer):
	
    beard_id = serializers.ReadOnlyField()

    player = serializers.SlugRelatedField(
        queryset=Player.objects.all(), slug_field='first_name'
    )
    class Meta:
        model = BeardModel
        fields = "__all__"


class BeardColorSerializer(serializers.ModelSerializer):
	
    player = serializers.SlugRelatedField(
        queryset=Player.objects.all(), slug_field='first_name'
    )

    class Meta:
        model = BeardColorModel
        fields = "__all__"


class ClothingSerializer(serializers.ModelSerializer):
	
    clothing_id = serializers.ReadOnlyField()

    player = serializers.SlugRelatedField(
        queryset=Player.objects.all(), slug_field='first_name'
    )
    class Meta:
        model = ClothingModel
        fields = "__all__"


class PantsSerializer(serializers.ModelSerializer):
	
    pants_id = serializers.ReadOnlyField()

    player = serializers.SlugRelatedField(
        queryset=Player.objects.all(), slug_field='first_name'
    )
    class Meta:
        model = PantsModel
        fields = "__all__"


class ShoesSerializer(serializers.ModelSerializer):
	
    shoes_id = serializers.ReadOnlyField()

    player = serializers.SlugRelatedField(
        queryset=Player.objects.all(), slug_field='first_name'
    )
    class Meta:
        model = ShoesModel
        fields = "__all__"



class BodyColorSerializer(serializers.ModelSerializer):
	

    player = serializers.SlugRelatedField(
        queryset=Player.objects.all(), slug_field='first_name'
    )
    class Meta:
        model = BodyColorModel
        fields = "__all__"




class PlayerSerializer(serializers.ModelSerializer):
    
    character_id = serializers.ReadOnlyField()


    hair_id = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='hair_id'
    )
    hair_color = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='hair_color'
    )
    eye_id= serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='eye_id'
    )
    eyebrow_id = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='eyebrow_id'
    )
    eyebrow_color=serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='eyebrow_color'
    )
    nose_id = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='nose_id'
    )
    mouth_id = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='mouth_id'
    )
    beard_id = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='beard_id'
    )
    beard_color = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='beard_color'
    )
    clothing_id = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='clothing_id'
    )
    pants_id = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='pants_id'
    )
    shoes_id =serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='shoes_id'
    )

    body_color =serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='body_color'
    )

    class Meta:
        model = Player
        read_only_fields = ('hair_id', )
        fields = "__all__"


