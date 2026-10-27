from .models import Client, Compte, Agent, DemandeCredit, Remboursement, Transaction
from rest_framework import viewsets
from .serializers import (
    ClientSerializer,
    CompteSerializer,
    AgentSerializer,
    DemandeCreditSerializer,
    RemboursementSerializer,
    TransactionSerializer,
)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class CompteViewSet(viewsets.ModelViewSet):
    queryset = Compte.objects.all()
    serializer_class = CompteSerializer


class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer


class DemandeCreditViewSet(viewsets.ModelViewSet):
    queryset = DemandeCredit.objects.all()
    serializer_class = DemandeCreditSerializer


class RemboursementViewSet(viewsets.ModelViewSet):
    queryset = Remboursement.objects.all()
    serializer_class = RemboursementSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
