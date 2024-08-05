<script setup lang="ts">
import {useWalletStore} from "~/store/wallet";
import singletonContractApi from "~/utils/api/contract";

const $walletStore = useWalletStore()
const selectedAssetsCount = computed(() => {
    return $walletStore.nfts.filter((asset) => {
        return !!$walletStore.selectedAssets[asset.nft_id]
    }).length
})
const buttonDisabled = computed(() => selectedAssetsCount.value <= 0 )

const contractApi = singletonContractApi

function bundleAssets() {
    const assets = $walletStore.nfts.filter((asset) => {
        return !!$walletStore.selectedAssets[asset.nft_id]
    })
    contractApi.bundle(assets)
    $walletStore.setIsUpdating(true)
}

</script>

<template>
<div class="bundle-wrap">
    <div class="bundle-info">Click on your assets to select & bundle them</div>
    <div class="bundle-selected">Selected assets: {{ selectedAssetsCount }}</div>
    <button class="bundle-button" :class="(buttonDisabled ? ' disabled': '')" :disabled="buttonDisabled" @click="bundleAssets()">BUNDLE</button>
</div>
</template>

<style scoped lang="scss">
.bundle-wrap {
    text-align: center;
    margin-top: 30px;
}

.bundle-info {
    font-size: 14px;
}

.bundle-selected {
    font-size: 18px;
}

.bundle-button {
    margin-top: 20px;
    font-size: 20px;
    background-color: #2ad238;
    border-radius: 100px;
    color: white;
    cursor: pointer;
    padding: 10px 20px;

    &.disabled {
        background-color: #cacaca;
    }
}

.bold {
    font-weight: bold;
}
</style>