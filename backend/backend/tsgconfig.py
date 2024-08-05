from django.conf import settings
from django_rest_tsg.build import build

from api.models.proxies.SimpleHash import WalletSerializer, TransactionResultSerializer, NftImagePropertiesSerializer, \
    NftPreviewSerializer, NftOwnersSerializer, NftContractSerializer, NftResultSerializer, \
    NftImagePropertiesLiteSerializer, NftMarketplacePageSerializer, NftCollectionSerializer, \
    NftCollectionRoyaltiesSerializer, NftFirstCreatedSerializer, NftRaritySerializer, NftRoyaltySerializer, \
    NftExtraMetadataSerializer

BUILD_DIR = settings.BASE_DIR / "../frontend/types"

BUILD_TASKS = [
    build(TransactionResultSerializer),
    build(NftPreviewSerializer),
    build(NftImagePropertiesSerializer),
    build(NftOwnersSerializer),
    build(NftContractSerializer),
    build(NftImagePropertiesLiteSerializer),
    build(NftMarketplacePageSerializer),
    build(NftCollectionRoyaltiesSerializer),
    build(NftCollectionSerializer),
    build(NftFirstCreatedSerializer),
    build(NftRaritySerializer),
    build(NftRoyaltySerializer),
    build(NftExtraMetadataSerializer),

    build(NftResultSerializer),
    build(WalletSerializer),
]
