from .views import LandNFTViewSet, LandViewSet, PetNFTViewSet, PetViewSet, PlayerViewSet, PlayerWalletViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'players', PlayerViewSet, basename='player')

router.register(r'players-wallet', PlayerWalletViewSet, basename='player-wallet')



router.register(r'pets', PetViewSet, basename='pet')

router.register(r'pets-nft', PetNFTViewSet, basename='pet-nft')

router.register(r'lands', LandViewSet, basename='land')

router.register(r'lands-nft', LandNFTViewSet, basename='land-nft')

urlpatterns = router.urls



