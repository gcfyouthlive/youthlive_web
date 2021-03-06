from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer,AyliveSerializer, EventsSerializer, TransactionSerializer
from .models import User,Aylive,Events,Transaction

# API
# Users
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('lastname')
    serializer_class = UserSerializer

# Ask.YouthLIVE
class AyliveViewSet(viewsets.ModelViewSet):
    queryset = Aylive.objects.all().order_by('timestamp')
    serializer_class = AyliveSerializer

# Events
class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all().order_by('datetime')
    serializer_class = EventsSerializer

# Transaction
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all().order_by('trans_date')
    serializer_class = TransactionSerializer

