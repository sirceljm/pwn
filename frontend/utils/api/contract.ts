import {createPublicClient, createWalletClient, custom, http, TransactionReceiptNotFoundError} from 'viem'
import {sepolia} from 'viem/chains'
import {abi} from "~/abi"
import {NftResult} from "~/types/nft-result"

class ContractApi {
    private address: `0x${string}` = "0x0"

    private watchInterval: number = 0
    public transactions = {} as {
        [key:`0x${string}`]: Boolean
    }
    private transactionsCallback = ((transactions: { [key:`0x${string}`]: Boolean }) => {})

    watchTransactions(callback: (transactions: { [key:`0x${string}`]: Boolean }) => void) {
        this.transactionsCallback = callback
    }

    private publicClient = createPublicClient({
        chain: sepolia,
        transport: http()
    })

    private walletClient = createWalletClient({
        chain: sepolia,
        transport: custom((window as any).ethereum!)
    })

    public constructor() {
        this.watchInterval = window.setInterval(() => {
            Object.keys(this.transactions).forEach((key) => {
                if (this.transactions[key as `0x${string}`] === false) {
                    this.publicClient.getTransactionReceipt({
                        hash: key as `0x${string}`
                    }).then((result) => {
                        this.transactions[key as `0x${string}`] = true
                        setTimeout(() => {
                            this.transactionsCallback(this.transactions)
                        }, 3000)
                    }).catch((err) => {
                        if (!(err instanceof TransactionReceiptNotFoundError)) {
                            throw err
                        }
                    })
                }
            })
        }, 1000)
    }

    async connectWallet() {
        const addresses = await this.walletClient.requestAddresses()
        if (addresses.length > 0) {
            this.setAddress(addresses[0])
            return addresses[0]
        } else {
            return null
        }
    }

    setAddress(address: `0x${string}`) {
        this.address = address
    }

    async bundle(assets: NftResult[]) {
        const args = [] as {
            category: number,
            assetAddress: `0x${string}`,
            id: bigint,
            amount: bigint
        }[]

        assets.forEach((asset) => {
            let category = 0
            switch (asset.contract.type) {
                case "ERC20": category = 0; break;
                case "ERC721": category = 1; break;
                case "ERC1155": category = 2; break;
            }

            args.push({
                category: category,
                assetAddress: asset.contract_address as `0x${string}`,
                id: BigInt(asset.token_id),
                amount: BigInt(asset.token_count)
            })
        })

        const transaction = await this.walletClient.writeContract({
            address: '0x448E3D0a4BAa00FE511a03E7B27177AeDE6d9636',
            abi: abi,
            functionName: 'create',
            args: [args],
            account: this.address
        })

        this.transactions[transaction] = false
    }

    async unbundle(tokenId: bigint) {
        const transaction = await this.walletClient.writeContract({
            address: '0x448E3D0a4BAa00FE511a03E7B27177AeDE6d9636',
            abi: abi,
            functionName: 'unwrap',
            args: [tokenId],
            account: this.address
        })

        this.transactions[transaction] = false
    }

    onDestroy()  {
        clearInterval(this.watchInterval)
    }
}

const singletonContractApi = new ContractApi()

export default singletonContractApi