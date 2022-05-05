from rest_framework import viewsets
from rest_framework.response import Response
from .models import Player
from .serializer import PlayerSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Player instances.
    """
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()