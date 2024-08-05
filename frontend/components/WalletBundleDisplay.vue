<script setup lang="ts">
import {useWalletStore} from "~/store/wallet";
import AssetCard from "~/components/AssetCard.vue";
const $walletStore = useWalletStore()

const assets = computed(() => {
    return $walletStore.nfts.filter((asset) => {
        return asset.name?.startsWith("Token Bundler")
    })
})

</script>

<template>
<div class="nft-container">
    <AssetCard v-for="asset in assets" :asset="asset"/>
</div>
</template>

<style scoped lang="scss">
.nft-container {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
    align-items: center;
    grid-gap: 30px;

    border-radius: 10px;
    border: 1px dashed lightgray;
    padding: 30px;
    background-color: white;
}
</style>