from rest_framework import serializers

from .models import Agent, Client, Compte, DemandeCredit, Remboursement, Transaction


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class CompteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compte
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'


class DemandeCreditSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemandeCredit
        fields = '__all__'


class RemboursementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Remboursement
        fields = '__all__'