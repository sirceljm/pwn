import json

from rest_framework import serializers


class TransactionResultSerializer(serializers.Serializer):
    nft_id = serializers.CharField()
    chain = serializers.CharField()
    contract_address = serializers.CharField()
    token_id = serializers.CharField()
    collection_id = serializers.CharField()
    event_type = serializers.CharField()
    from_address = serializers.CharField()
    to_address = serializers.CharField()
    quantity = serializers.CharField()
    quantity_string = serializers.CharField()
    timestamp = serializers.CharField()
    block_number = serializers.CharField()
    block_hash = serializers.CharField()
    transaction = serializers.CharField()
    transaction_initiator = serializers.CharField()
    log_index = serializers.CharField()
    batch_transfer_index = serializers.CharField()
    sale_details = serializers.CharField()


class NftPreviewSerializer(serializers.Serializer):
    image_small_url = serializers.CharField()
    image_medium_url = serializers.CharField()
    image_large_url = serializers.CharField()
    image_opengraph_url = serializers.CharField()
    blurhash = serializers.CharField()
    predominant_color = serializers.CharField()


class NftImagePropertiesSerializer(serializers.Serializer):
    width = serializers.IntegerField()
    height = serializers.IntegerField()
    size = serializers.IntegerField()
    mime_type = serializers.CharField()
    exif_orientation = serializers.CharField()
    predominant_color = serializers.CharField()


class NftOwnersSerializer(serializers.Serializer):
    owner_address = serializers.CharField()
    quantity = serializers.IntegerField()
    quantity_string = serializers.CharField()
    first_acquired_date = serializers.CharField()
    last_acquired_date = serializers.CharField()


class NftContractSerializer(serializers.Serializer):
    type = serializers.CharField()
    name = serializers.CharField()
    symbol = serializers.CharField()
    deployed_via_contract = serializers.CharField()
    owned_by = serializers.CharField()
    has_multiple_collections = serializers.CharField()


class NftImagePropertiesLiteSerializer(serializers.Serializer):
    width = serializers.IntegerField()
    height = serializers.IntegerField()
    mime_type = serializers.CharField()


class NftMarketplacePageSerializer(serializers.Serializer):
    marketplace_id = serializers.CharField()
    marketplace_name = serializers.CharField()
    marketplace_collection_id = serializers.CharField()
    nft_url = serializers.CharField()
    collection_url = serializers.CharField()
    verified = serializers.BooleanField()


class NftCollectionRoyaltiesSerializer(serializers.Serializer):
    source = serializers.CharField()
    total_creator_fee_basis_points = serializers.CharField()
    recipients = serializers.ListSerializer(
        child=serializers.CharField()
    )


class NftCollectionSerializer(serializers.Serializer):
    collection_id = serializers.CharField()
    name = serializers.CharField()
    description = serializers.CharField()
    image_url = serializers.CharField()
    image_properties = NftImagePropertiesSerializer()
    banner_image_url = serializers.CharField()
    category = serializers.CharField()
    is_nsfw = serializers.CharField()
    external_url = serializers.CharField()
    twitter_username = serializers.CharField()
    discord_url = serializers.CharField()
    instagram_username = serializers.CharField()
    medium_username = serializers.CharField()
    telegram_url = serializers.CharField()
    marketplace_pages = serializers.ListSerializer(
        child=NftMarketplacePageSerializer()
    )
    metaplex_mint = serializers.CharField()
    metaplex_candy_machine = serializers.CharField()
    metaplex_first_verified_creator = serializers.CharField()
    floor_prices = serializers.CharField()
    top_bids = serializers.CharField()
    distinct_owner_count = serializers.IntegerField()
    distinct_nft_count = serializers.IntegerField()
    total_quantity = serializers.IntegerField()
    chains = serializers.ListSerializer(
        child=serializers.CharField()
    )
    top_contracts = serializers.ListSerializer(
        child=serializers.CharField()
    )
    collection_royalties = serializers.ListSerializer(
        child=NftCollectionRoyaltiesSerializer()
    )


class NftFirstCreatedSerializer(serializers.Serializer):
    minted_to = serializers.CharField()
    quantity = serializers.IntegerField()
    quantity_string = serializers.CharField()
    timestamp = serializers.CharField()
    block_number = serializers.IntegerField()
    transaction = serializers.CharField()
    transaction_initiator = serializers.CharField()


class NftRaritySerializer(serializers.Serializer):
    rank = serializers.CharField()
    score = serializers.CharField()
    unique_attributes = serializers.CharField()


class NftRoyaltySerializer(serializers.Serializer):
    source = serializers.CharField()
    total_creator_fee_basis_points = serializers.IntegerField()
    recipients = serializers.ListSerializer(
        child=serializers.CharField()
    )


class NftExtraMetadataSerializer(serializers.Serializer):
    attributes = serializers.ListSerializer(
        child=serializers.CharField()
    )
    image_original_url = serializers.CharField()
    animation_original_url = serializers.CharField()
    metadata_original_url = serializers.CharField()


class NftResultSerializer(serializers.Serializer):
    nft_id = serializers.CharField()
    chain = serializers.CharField()
    contract_address = serializers.CharField()
    token_id = serializers.CharField()
    name = serializers.CharField()
    description = serializers.CharField()
    previews = NftPreviewSerializer()
    image_url = serializers.CharField()
    image_properties = serializers.ListSerializer(
        child=NftImagePropertiesLiteSerializer()
    )
    video_url = serializers.CharField()
    video_properties = serializers.CharField()
    audio_url = serializers.CharField()
    audio_properties = serializers.CharField()
    model_url = serializers.CharField()
    model_properties = serializers.CharField()
    other_url = serializers.CharField()
    other_properties = serializers.CharField()
    background_color = serializers.CharField()
    external_url = serializers.CharField()
    created_date = serializers.CharField()
    status = serializers.CharField()
    token_count = serializers.IntegerField()
    owner_count = serializers.IntegerField()
    owners = serializers.ListSerializer(
        child=NftOwnersSerializer()
    )
    contract = NftContractSerializer()
    collection = NftCollectionSerializer()
    last_sale = serializers.CharField()
    primary_sale = serializers.CharField()
    first_created = NftFirstCreatedSerializer()
    rarity = NftRaritySerializer()
    royalty = serializers.ListSerializer(
        child=NftRoyaltySerializer()
    )
    extra_metadata = NftExtraMetadataSerializer()


class WalletSerializer(serializers.Serializer):
    nfts = serializers.ListField(
        child=NftResultSerializer()
    )

