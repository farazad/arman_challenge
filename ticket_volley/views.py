from rest_framework import viewsets
from django.contrib.auth import get_user_model
from .models import Stadium, Match, Seat
from .serializers import UserSerializer, StadiumSerializer, MatchSerializer, SeatSerializer


User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class StadiumViewSet(viewsets.ModelViewSet):
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer