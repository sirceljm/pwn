<script setup lang="ts">
import {useWalletStore} from "~/store/wallet";
import {NftResult} from "~/types/nft-result";
import singletonContractApi from "~/utils/api/contract";
const $walletStore = useWalletStore()

const contractApi = singletonContractApi

const {asset} = defineProps<{
    asset: NftResult
}>()

const isBundle = computed(() => {
    return asset.name?.startsWith("Token Bundler")
})

function isSelected(id: string) {
    return $walletStore.selectedAssets[id]
}

function toggleSelect(id: string) {
    $walletStore.selectedAssets[id] = !$walletStore.selectedAssets[id]
}

function unbundle(event: Event, tokenId: string) {
    event.stopPropagation()
    contractApi.unbundle(BigInt(tokenId))
    $walletStore.setIsUpdating(true)
}
</script>

<template>
<div class="nft" :class="(isSelected(asset.nft_id) ? ' selected' : '')"  @click="() => toggleSelect(asset.nft_id)">
    <div class="nft-title"></div>
    <img class="preview-image" :src="asset.previews.image_large_url"  alt="nft image"/>
    <div>{{ asset.name }}</div>
    <div>Ammount: <span class="bold">{{ asset.token_count }}</span></div>
    <div class="nft-description">{{ asset.description }}</div>
    <button class="unbundle-button" v-if="isBundle" @click="(event) => {unbundle(event, asset.token_id)}">Unbundle</button>
</div>
</template>

<style scoped>
.nft {
    cursor: pointer;
    width: 200px;
    border-radius: 8px;
    border: 1px solid black;
    box-shadow: 2px 2px 6px #000;
    display: flex;
    align-items: center;
    flex-direction: column;
    justify-content: space-between;
    padding: 10px;
    justify-self: center;
    text-align: center;

    &.selected {
        background-color: #8eedff;
    }

    .preview-image {
        width: 100px;
    }

    .nft-description {
        color: gray;
        font-size: 10px;
    }

    .bold {
        font-weight: bold;
    }

    .unbundle-button {
        margin-top: 10px;
        font-size: 14px;
        background-color: #e31d1d;
        border-radius: 100px;
        color: white;
        cursor: pointer;
        padding: 10px 20px;

        &.disabled {
            background-color: #cacaca;
        }
    }
}
</style>