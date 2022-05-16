from .views import BeardColorViewSet, BeardViewSet, BodyColorViewSet, ClothingViewSet, EyeBrowColorViewSet, EyeBrowViewSet, EyeViewSet, HairColorViewSet, MouthViewSet, NoseViewSet, PantsViewSet, PlayerViewSet, PlayerWalletViewSet, HairViewSet, ShoesViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'players', PlayerViewSet, basename='player')

router.register(r'hairs', HairViewSet, basename='hair')
router.register(r'haircolor', HairColorViewSet, basename='hair_color')
router.register(r'eyes', EyeViewSet, basename='eye')
router.register(r'eyebrows', EyeBrowViewSet, basename='eyebrow')
router.register(r'eyebrowscolor', EyeBrowColorViewSet, basename='eyebrowcolor')
router.register(r'nose', NoseViewSet, basename='nose')
router.register(r'mouth', MouthViewSet, basename='mouth')
router.register(r'beard', BeardViewSet, basename='beard')
router.register(r'beardcolors', BeardColorViewSet, basename='beardcolor')
router.register(r'clothings', ClothingViewSet, basename='clothing')
router.register(r'pants', PantsViewSet, basename='pant')
router.register(r'shoes', ShoesViewSet, basename='shoe')
router.register(r'bodycolors', BodyColorViewSet, basename='bodycolor')

router.register(r'players-wallet', PlayerWalletViewSet, basename='player-wallet')
urlpatterns = router.urls