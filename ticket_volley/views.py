from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
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
    
    @action(detail=True, methods=['post'])
    def reserve(self, request, pk=None):
        seat = self.get_object()
        if not seat.is_reserved:
            seat.is_reserved = True
            seat.save()
            return Response({'message': 'Seat reserved successfully'})
        else:
            return Response({'message': 'Seat already reserved'}, status=status.HTTP_409_CONFLICT)