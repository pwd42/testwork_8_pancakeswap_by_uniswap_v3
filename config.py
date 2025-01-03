# https://docs.pancakeswap.finance/developers/smart-contracts/pancakeswap-exchange/v3-contracts#address

import json

RPC_URLS = {
    "Arbitrum": "https://endpoints.omniatech.io/v1/arbitrum/one/public",
    "Optimism": "https://op-pokt.nodies.app",
    # "Base": "https://1rpc.io/base"
    # "Base": "https://base-pokt.nodies.app"
    # "Base": "https://base.meowrpc.com"
    "Base": "https://base.drpc.org"
}

EXPLORERS_URL = {
    "Arbitrum": "https://arbiscan.io/",
    "Optimism": "https://optimistic.etherscan.io/",
    "Base": "https://basescan.org/"
}

CHAIN_ID_BY_NAME = {
    'Arbitrum': 42161,
    'Optimism': 10,
    'Base': 8453
}

ETH_MASK = "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE"
ZERO_ADDRESS = "0x0000000000000000000000000000000000000000"

PANCAKESWAP_CONTRACTS = {
    'Arbitrum': {
        'quoter': '0xB048Bbc1Ee6b733FFfCFb9e9CeF7375518e25997',
        'router': '0x1b81D678ffb9C0263b24A97847620C99d213eB14'
    },
    'Base': {
        'quoter': '0xB048Bbc1Ee6b733FFfCFb9e9CeF7375518e25997',
        'router': '0x1b81D678ffb9C0263b24A97847620C99d213eB14'
    }
}

UNISWAP_CONTRACTS = {
    'Arbitrum': {
        'quoter': '0xb27308f9F90D607463bb33eA1BeBb41C27CE5AB6',
        'router': '0xE592427A0AEce92De3Edee1F18E0157C05861564'
    }
}

#делаем ETH как WETH, как указано в документации Uniswap_V2
#https://docs.uniswap.org/contracts/v2/reference/smart-contracts/router-02#swapexacttokensforeth

TOKENS_PER_CHAIN = {
    'Arbitrum': {
        "ETH": "0x82aF49447D8a07e3bd95BD0d56f35241523fBab1",
        # "WETH": "0x82aF49447D8a07e3bd95BD0d56f35241523fBab1"
        "USDC": "0xaf88d065e77c8cC2239327C5EDb3A432268e5831"
    },
    'Optimism': {
        "ETH": "0x4200000000000000000000000000000000000006",
        # "WETH": "0x4200000000000000000000000000000000000006",
        "USDC":"0x0b2C639c533813f4Aa9D7837CAf62653d097Ff85"
    },
    'Base': {
        "ETH" : "0x4200000000000000000000000000000000000006",
        # "ETH": "0x0000000000000000000000000000000000000000",
        # "WETH": "0x4200000000000000000000000000000000000006",
        "USDC": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913"
    }
}

with open('erc20_abi.json') as file:
    ERC20_ABI = json.load(file)

with open('pancakeswap_quoterV2.json') as file:
    PANCAKESWAP_QUOTER_V2_ABI = json.load(file)

with open('pancakeswap_routerV3.json') as file:
    PANCAKESWAP_ROUTER_V3_ABI = json.load(file)
