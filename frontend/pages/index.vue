<script setup lang="ts">
import '~/assets/css/global.css'

import {useWalletStore} from "~/store/wallet";
import singletonContractApi from "~/utils/api/contract";

const $walletStore = useWalletStore()

onMounted(async () => {
    singletonContractApi.watchTransactions(async (transactions) => {
        $walletStore.invalidateCache()
        $walletStore.setIsUpdating(false)
    })

    $walletStore.setAddress(await singletonContractApi.connectWallet())
    $walletStore.invalidateCache()
})
</script>

<template>
    <RefreshingInfo />

    <div class="title">PWN CHALLENGE</div>
    <WalletAddrDisplay class="wallet"/>
    <InvalidateButton />

    <SelectedAssetsInfo />

    <div class="nfts-title-bundles">MY BUNDLES</div>
    <WalletBundleDisplay />

    <div class="nfts-title-assets">MY ASSETS</div>
    <WalletAssetDisplay />

</template>

<style scoped>

.title {
    text-align: center;
    font-size: 36px;
}

.nfts-title-bundles {
    text-align: center;
    margin-top: 20px;
    margin-bottom: 10px;
}
.nfts-title-assets {
    margin-top: 20px;
    text-align: center;
    margin-bottom: 10px;
}
</style>