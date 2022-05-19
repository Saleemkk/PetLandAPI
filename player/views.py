from rest_framework import viewsets
from rest_framework.response import Response
from .models import Land, Pet, Player
from .serializer import LandSerializer, PetSerializer, PlayerSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Player instances.
    """
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()


class PlayerWalletViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Player instances.
    """
    lookup_field = 'wallet_address'
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()


class PetViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Player instances.
    """
    serializer_class = PetSerializer
    queryset = Pet.objects.all()


class PetNFTViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Player instances.
    """
    lookup_field = 'wallet_address'
    serializer_class = PetSerializer
    queryset = Pet.objects.all()


class LandViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Player instances.
    """
    serializer_class = LandSerializer
    queryset = Land.objects.all()


class LandNFTViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Player instances.
    """
    lookup_field = 'wallet_address'
    serializer_class = LandSerializer
    queryset = Land.objects.all()

