<script setup lang="ts">

import {useWalletStore} from "~/store/wallet";

const $walletStore = useWalletStore()

function invalidate(): void {
    $walletStore.invalidateCache()
}

</script>

<template>
    <div class="invalidate-wrap">
        <button class="invalidate-button" @click="invalidate()">Invalidate assets</button>
    </div>
</template>

<style scoped>
.invalidate-wrap {
    text-align: center;
}
.invalidate-button {
    margin-top: 20px;
    font-size: 20px;
    background-color: #2aabd2;
    border-radius: 100px;
    color: white;
    cursor: pointer;
    padding: 10px 20px;
}
</style>