import json

from rest_framework.response import Response
from rest_framework.decorators import api_view

import requests

from api.models.db.Wallet import Wallet
from api.models.proxies.SimpleHash import TransactionResultSerializer, NftPreviewSerializer, WalletSerializer

SIMPLEHASH_API_KEY = "sirceljm_sk_fliew8wozr393e96ib3zdeuck8ifstzj"

headers = {
    "accept": "application/json",
    "X-API-KEY": SIMPLEHASH_API_KEY
}


@api_view(['GET'])
def health(request):
    return Response({'success': True})


# @api_view(['GET'])
# def get_wallet_balances(request):
#     address = request.GET.get('address', 'default')
#     url = f"https://api.simplehash.com/api/v0/native_tokens/balances?chains=ethereum-sepolia,bsc-testnet&wallet_addresses={address}"
#     headers = {
#         "accept": "application/json",
#         "X-API-KEY": SIMPLEHASH_API_KEY
#     }
#
#     response = requests.get(url, headers=headers)
#     return Response(response.json())


@api_view(['GET'])
def get_wallet_nfts(request):
    address = request.GET.get('address', 'default')
    wallet = Wallet.objects.get_or_create(wallet_id=address)

    if wallet[0].nfts is not None:
        return Response(wallet[0].nfts)
    else:
        url = f"https://api.simplehash.com/api/v0/nfts/owners?chains=ethereum-sepolia&wallet_addresses={address}"
        response = requests.get(url, headers=headers)
        wallet[0].nfts = response.json()['nfts']
        wallet[0].save()
        return Response(wallet[0].nfts)


# @api_view(['GET'])
# def get_wallet_fungibles(request):
#     address = request.GET.get('address', 'default')
#     wallet = Wallet.objects.get_or_create(wallet_id=address)
#
#     if wallet[0].fungibles is not None:
#         fungibles = TransactionResultSerializer(wallet[0].fungibles)
#         return Response(fungibles.data)
#     else:
#         url = f"https://api.simplehash.com/api/v0/fungibles/balances?chains=ethereum-sepolia,bsc-testnet&wallet_addresses={address}"
#         response = requests.get(url, headers=headers)
#         # fungibles = TransactionResultSerializer(response.json()['fungibles'])
#         #
#         # wallet[0].fungibles = fungibles.data
#         # wallet[0].save()
#
#         return Response(response.json()['fungibles'])

# @api_view(['GET'])
# def get_wallet_contracts(request):
#     address = request.GET.get('address', 'default')
#     wallet = Wallet.objects.get_or_create(wallet_id=address)
#
#     if wallet[0].contracts is not None:
#         contracts = TransactionResultSerializer(wallet[0].contracts)
#         return Response(contracts.data)
#     else:
#         url = f"https://api.simplehash.com/api/v0/nfts/contracts_by_wallets?chains=ethereum-sepolia,bsc-testnet&wallet_addresses={address}"
#         response = requests.get(url, headers=headers)
#         # contracts = TransactionResultSerializer(response.json()['contracts'])
#         #
#         # wallet[0].contracts = contracts.data
#         # wallet[0].save()
#
#         return Response(response.json())


# @api_view(['GET'])
# def get_wallet_transactions(request):
#     address = request.GET.get('address', 'default')
#
#     wallet = Wallet.objects.get_or_create(wallet_id=address)
#     if wallet[0].transactions is not None:
#         transactions = TransactionResultSerializer(wallet[0].transactions)
#         return Response(transactions.data)
#     else:
#         url = f"https://api.simplehash.com/api/v0/nfts/transfers/wallets?chains=ethereum-sepolia,bsc-testnet&wallet_addresses={address}"
#         response = requests.get(url, headers=headers)
#         transfers = TransactionResultSerializer(response.json()['transfers'])
#
#         wallet[0].transactions = transfers.data
#         wallet[0].save()
#
#         return Response(wallet[0].transactions)


@api_view(['GET'])
def invalidate(request):
    address = request.GET.get('address', 'default')

    wallet = Wallet.objects.get_or_create(wallet_id=address)
    wallet[0].nfts = None
    wallet[0].save()

    url = f"https://api.simplehash.com/api/v0/nfts/owners?chains=ethereum-sepolia&wallet_addresses={address}"
    response = requests.get(url, headers=headers)
    wallet[0].nfts = response.json()['nfts']
    wallet[0].save()
    return Response(wallet[0].nfts)
