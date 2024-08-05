import {NftResult} from "~/types/nft-result"

class BackendApi {
    async getAssets(address: `0x${string}`): Promise<NftResult[]> {
        const {data: data} = await useFetch(`http://localhost:8000/api/wallet/nfts?address=${address}`)
        return data.value as NftResult[]
    }

    async invalidateCache(address: `0x${string}`): Promise<NftResult[]> {
        const {data: data} = await useFetch(`http://localhost:8000/api/wallet/invalidate?address=${address}`)
        return data.value as NftResult[]
    }
}

const singletonBackendApi = new BackendApi()

export default singletonBackendApi