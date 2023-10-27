import json
from pathlib import Path

with open('data/rpc.json') as file:
    RPC = json.load(file)

with open('data/abi/erc20_abi.json') as file:
    ERC20_ABI = json.load(file)

with open("accounts.txt", "r") as file:
    ACCOUNTS = [row.strip() for row in file]

with open("proxy.txt", "r") as file:
    PROXIES = [row.strip() for row in file]

with open('data/abi/zksync/deposit.json') as file:
    ZKSYNC_DEPOSIT_ABI = json.load(file)

with open('data/abi/zksync/withdraw.json') as file:
    ZKSYNC_WITHDRAW_ABI = json.load(file)

with open('data/abi/zksync/weth.json') as file:
    WETH_ABI = json.load(file)

with open("data/abi/zkswap/router.json", "r") as file:
    ZKSWAP_ROUTER_ABI = json.load(file)

with open("data/abi/reactorfusion/abi.json", "r") as file:
    REACTORFUSION_ABI = json.load(file)

with open("data/abi/l2telegraph/send_message.json", "r") as file:
    L2TELEGRAPH_MESSAGE_ABI = json.load(file)

with open("data/abi/l2telegraph/bridge_nft.json", "r") as file:
    L2TELEGRAPH_NFT_ABI = json.load(file)

with open("data/abi/nft2me/abi.json", "r") as file:
    MINTER_ABI = json.load(file)

with open("data/abi/mailzero/abi.json", "r") as file:
    MAILZERO_ABI = json.load(file)

with open("data/abi/tavaera/id.json", "r") as file:
    TAVAERA_ID_ABI = json.load(file)

with open("data/abi/tavaera/abi.json", "r") as file:
    TAVAERA_ABI = json.load(file)

with open("data/abi/zks/abi.json", "r") as file:
    ZKS_ABI = json.load(file)

with open("data/abi/omnisea/abi.json", "r") as file:
    OMNISEA_ABI = json.load(file)

with open("data/abi/gnosis/abi.json", "r") as file:
    SAFE_ABI = json.load(file)

ZKSYNC_BRIDGE_CONTRACT = "0x32400084c286cf3e17e7b677ea9583e60a000324"

CONTRACT_PATH = Path("data/deploy/Token.json")

ZERO_ADDRESS = "0x0000000000000000000000000000000000000000"

ZKSYNC_TOKENS = {
    "ETH": "0x5aea5775959fbc2557cc8789bc1bf90a239d9a91",
    "WETH": "0x5aea5775959fbc2557cc8789bc1bf90a239d9a91",
    "USDC": "0x3355df6D4c9C3035724Fd0e3914dE96A5a83aaf4",
    "USDT": "0x493257fd37edb34451f62edf8d2a0c418852ba4c",
    "BUSD": "0x2039bb4116b4efc145ec4f0e2ea75012d6c0f181",
    "MATIC": "0x28a487240e4d45cff4a2980d334cc933b7483842",
    "OT": "0xd0ea21ba66b67be636de1ec4bd9696eb8c61e9aa",
    "MAV": "0x787c09494ec8bcb24dcaf8659e7d5d69979ee508",
    "WBTC": "0xbbeb516fb02a01611cbbe0453fe3c580d7281011",
}


ZKSWAP_CONTRACTS = {
    "router": "0x18381c0f738146Fb694DE18D1106BdE2BE040Fa4"
}

REACTORFUSION_CONTRACTS = {
    "landing": "0xC5db68F30D21cBe0C9Eac7BE5eA83468d69297e6",
    "collateral": "0x23848c28af1c3aa7b999fa57e6b6e8599c17f3f2",
}

L2TELEGRAPH_MESSAGE_CONTRACT = "0x0d4a6d5964f3b618d8e46bcfbf2792b0d769fbda"

L2TELEGRAPH_NFT_CONTRACT = "0xD43A183C97dB9174962607A8b6552CE320eAc5aA"

MAILZERO_CONTRACT = "0xc94025c2eA9512857BD8E1e611aB9b773b769350"

TAVAERA_ID_CONTRACT = "0xd29Aa7bdD3cbb32557973daD995A3219D307721f"

TAVAERA_CONTRACT = "0x50b2b7092bcc15fbb8ac74fe9796cf24602897ad"

ZKS_CONTRACT = "0xcbe2093030f485adaaf5b61deb4d9ca8adeae509"

OMNISEA_CONTRACT = "0x1Ecd053f681a51E37087719653f3f0FFe54750C0"

SAFE_CONTRACT = "0xDAec33641865E4651fB43181C6DB6f7232Ee91c2"
