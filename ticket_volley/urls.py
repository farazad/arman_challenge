from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, StadiumViewSet, MatchViewSet, SeatViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'stadiums', StadiumViewSet)
router.register(r'matches', MatchViewSet)
router.register(r'seats', SeatViewSet)

urlpatterns = [
    path('', include(router.urls)),
]