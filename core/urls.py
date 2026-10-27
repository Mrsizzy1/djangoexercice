from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    AgentViewSet,
    ClientViewSet,
    CompteViewSet,
    DemandeCreditViewSet,
    RemboursementViewSet,
    TransactionViewSet,
)

router = DefaultRouter()
router.register(r'clients', ClientViewSet, basename='client')
router.register(r'comptes', CompteViewSet, basename='compte')
router.register(r'agents', AgentViewSet, basename='agent')
router.register(r'demandes-credit', DemandeCreditViewSet, basename='demande-credit')
router.register(r'remboursements', RemboursementViewSet, basename='remboursement')
router.register(r'transactions', TransactionViewSet, basename='transaction')

urlpatterns = [
    path('', include(router.urls)),
]
