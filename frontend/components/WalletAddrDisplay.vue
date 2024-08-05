<script setup lang="ts">
import {useWalletStore} from "~/store/wallet";
const $walletStore = useWalletStore()
</script>

<template>
    <div class="wallet">
        <div class="wallet-title">Wallet</div>
        <div class="wallet-address">{{ $walletStore.address }}</div>
    </div>
</template>

<style scoped>
.wallet {
    text-align: center;

    .wallet-title {
        font-size: 40px;
    }

    .wallet-address {
        font-size: 20px;
    }
}
</style>