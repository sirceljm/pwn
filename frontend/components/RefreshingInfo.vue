<script setup lang="ts">
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import {useWalletStore} from "~/store/wallet";
const $walletStore = useWalletStore()

</script>

<template>
<div class="refresh-wrap">
    <FontAwesomeIcon v-if="$walletStore.isUpdating" :icon="['fas', 'arrows-rotate']" spin />
</div>
</template>

<style scoped lang="scss">
.refresh-wrap {
    position: fixed;
    text-align: right;
    top: 20px;
    right: 30px;
    color: red;
    font-size: 50px;
}
</style>