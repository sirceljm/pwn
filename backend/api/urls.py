from django.urls import path
from . import views

urlpatterns = [
    path('health', views.health),
    # path('wallet/balances', views.get_wallet_balances),
    path('wallet/nfts', views.get_wallet_nfts),
    # path('wallet/fungibles', views.get_wallet_fungibles),
    # path('wallet/contracts', views.get_wallet_contracts),
    # path('wallet/transactions', views.get_wallet_transactions),
    path('wallet/invalidate', views.invalidate),
]

