import asyncio
from modules import *
from settings import NFTS2ME_CONTRACTS


async def deposit_reactorfusion(account_id, key, proxy):
    """
    Make deposit on ReactorFusion
    ______________________________________________________
    make_withdraw - True, if need withdraw after deposit

    all_amount - deposit from min_percent to max_percent
    """
    min_amount = 0.0001
    max_amount = 0.0002
    decimal = 5

    sleep_from = 5
    sleep_to = 24

    make_withdraw = True

    all_amount = False

    min_percent = 60
    max_percent = 80

    reactorfusion = ReactorFusion(account_id, key, proxy)
    await reactorfusion.deposit(
        min_amount, max_amount, decimal, sleep_from, sleep_to, make_withdraw, all_amount, min_percent, max_percent
    )


async def bridge_nft(account_id, key, proxy):
    """
    Make mint NFT and bridge NFT on L2Telegraph
    """

    sleep_from = 5
    sleep_to = 20

    l2telegraph = L2Telegraph(account_id, key, proxy)
    await l2telegraph.bridge(sleep_from, sleep_to)


async def mint_tavaera(account_id, key, proxy):
    """
    Mint Tavaera ID and Tavaera NFT
    """

    sleep_from = 5
    sleep_to = 20

    tavaera_nft = Tavaera(account_id, key, proxy)
    await tavaera_nft.mint(sleep_from, sleep_to)


async def mint_nft(account_id, key, proxy):
    """
    Mint NFT on NFTS2ME
    ______________________________________________________
    contracts - list NFT contract addresses
    """

    if len(NFTS2ME_CONTRACTS) > 0:
        contracts = NFTS2ME_CONTRACTS

        minter = Minter(account_id, key, proxy)
        await minter.mint_nft(contracts)
    else:
        print("No settings for NFTS2ME_CONTRACTS")


async def custom_routes(account_id, key, proxy):
    """
    LANDING:
        – deposit_reactorfusion, withdraw_reactorfusion,
    NFT/DOMAIN:
        – create_omnisea
        – bridge_nft
        – mint_tavaera
        – mint_nft
        – mint_mailzero_nft
        – mint_zks_domain
    ANOTHER:
        – send_message (l2Telegraph)
        – create_safe
    ______________________________________________________
    Disclaimer - You can add modules to [] to select random ones,
    example [module_1, module_2, [module_3, module_4], module 5]
    The script will start with module 1, 2, 5 and select a random one from module 3 and 4
    """

    use_modules = [
        [mint_tavaera, create_omnisea],
        [deposit_reactorfusion],
        [mint_zks_domain]
    ]

    sleep_from = 300
    sleep_to = 700

    random_module = True

    routes = Routes(account_id, key, proxy)
    await routes.start(use_modules, sleep_from, sleep_to, random_module)


#########################################
########### NO NEED TO CHANGE ###########
#########################################


async def send_message(account_id, key, proxy):
    l2telegraph = L2Telegraph(account_id, key, proxy)
    await l2telegraph.send_message()


async def mint_mailzero_nft(account_id, key, proxy):
    mint_nft = MailZero(account_id, key, proxy)
    await mint_nft.mint()


async def mint_zks_domain(account_id, key, proxy):
    zks_domain = ZKSDomain(account_id, key, proxy)
    await zks_domain.mint()


async def withdraw_reactorfusion(account_id, key, proxy):
    reactorfusion = ReactorFusion(account_id, key, proxy)
    await reactorfusion.withdraw()


async def create_omnisea(account_id, key, proxy):
    omnisea = Omnisea(account_id, key, proxy)
    await omnisea.create()


async def create_safe(account_id, key, proxy):
    gnosis_safe = GnosisSafe(account_id, key, proxy)
    await gnosis_safe.create_safe()


def get_tx_count():
    asyncio.run(check_tx())
