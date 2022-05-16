from rest_framework import viewsets
from rest_framework.response import Response
from .models import BeardColorModel, BeardModel, BodyColorModel, ClothingModel, EyeBrowColorModel, EyeBrowModel, EyeModel, HairColorModel, MouthModel, NoseModel, PantsModel, Player, HairModel, ShoesModel
from .serializer import BeardColorSerializer, BeardSerializer, BodyColorSerializer, ClothingSerializer, EyeBrowColorSerializer, EyeBrowSerializer, EyeSerializer, HairColorSerializer, MouthSerializer, NoseSerializer, PantsSerializer, PlayerSerializer, HairSerializer, ShoesSerializer


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


class HairViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Player instances.
    """
    serializer_class = HairSerializer
    queryset = HairModel.objects.all()



class HairColorViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Player instances.
    """
    serializer_class = HairColorSerializer
    queryset = HairColorModel.objects.all()


class EyeViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Player instances.
    """
    serializer_class = EyeSerializer
    queryset = EyeModel.objects.all()


class EyeBrowViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Player instances.
    """
    serializer_class = EyeBrowSerializer
    queryset = EyeBrowModel.objects.all()


class EyeBrowColorViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Player instances.
    """
    serializer_class = EyeBrowColorSerializer
    queryset = EyeBrowColorModel.objects.all()


class NoseViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Player instances.
    """
    serializer_class = NoseSerializer
    queryset =NoseModel.objects.all()



class MouthViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Player instances.
    """
    serializer_class = MouthSerializer
    queryset = MouthModel.objects.all()


class BeardViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Player instances.
    """
    serializer_class = BeardSerializer
    queryset = BeardModel.objects.all()


class BeardColorViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Player instances.
    """
    serializer_class = BeardColorSerializer
    queryset = BeardColorModel.objects.all()


class ClothingViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Player instances.
    """
    serializer_class = ClothingSerializer
    queryset = ClothingModel.objects.all()


class PantsViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Player instances.
    """
    serializer_class = PantsSerializer
    queryset = PantsModel.objects.all()



class ShoesViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Player instances.
    """
    serializer_class = ShoesSerializer
    queryset = ShoesModel.objects.all()


class BodyColorViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Player instances.
    """
    serializer_class = BodyColorSerializer
    queryset = BodyColorModel.objects.all()