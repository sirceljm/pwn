import {defineStore, Store} from 'pinia'
import {NftResult} from "~/types/nft-result";
import singletonBackendApi from "~/utils/api/backend";

export const useWalletStore = defineStore('wallet', {
    state: () => {
        return {
            address: null as `0x${string}` | null,
            nfts: [] as NftResult[],
            selectedAssets: {} as {
                [key:string]: Boolean
            },
            isUpdating: false
        };
    },

    actions: {
        setAddress(address: `0x${string}` | null) {
            this.address = address
        },
        async invalidateCache() {
            if (this.address != null) {
                this.isUpdating = true
                this.nfts = await singletonBackendApi.invalidateCache(this.address)
                setTimeout(() => {
                    this.isUpdating = false
                }, 1000)
            }
        },

        async reloadAssets() {
            if (this.address != null) {
                this.nfts = await singletonBackendApi.getAssets(this.address)
            }
        },

        setIsUpdating(isUpdating: boolean) {
            this.isUpdating = isUpdating
        }
    }
})