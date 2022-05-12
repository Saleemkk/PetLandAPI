from .views import PlayerViewSet, PlayerWalletViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'players', PlayerViewSet, basename='player')
router.register(r'players-wallet', PlayerWalletViewSet, basename='player-wallet')
urlpatterns = router.urls