from django.db import models
from rest_framework import serializers


class Wallet(models.Model):
    wallet_id = models.CharField(max_length=200, primary_key=True)
    nfts = models.JSONField(null=True)
    # fungibles = models.JSONField(null=True)
    # contracts = models.JSONField(null=True)
    # native = models.JSONField(null=True)
    # transactions = models.JSONField(null=True)

