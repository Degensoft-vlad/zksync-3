import random
import sys
import socket

import questionary
from loguru import logger
from questionary import Choice
from typing import Union

import requests
from config import ACCOUNTS, PROXIES
from decryption import decrypt_private_key
from settings import (USE_PROXY,
                      USE_MOBILE_PROXY,
                      MOBILE_PROXY,
                      CHANGE_PROXY_URL,
                      RANDOM_WALLET,
                      SLEEP_FROM,
                      SLEEP_TO,
                      DECRYPT_ACCOUNTS,
                      DECRYPT_ACCOUNTS_PASS)
from modules_settings import *


def get_module():
    result = questionary.select(
        "Select a method to get started",
        choices=[
            Choice("1) Deposit ReactorFusion", deposit_reactorfusion),
            Choice("2) Withdraw ReactorFusion", withdraw_reactorfusion),
            Choice("3) Mint and bridge NFT L2Telegraph", bridge_nft),
            Choice("4) Mint Tavaera ID + NFT", mint_tavaera),
            Choice("5) Mint NFT on NFTS2ME", mint_nft),
            Choice("6) Create NFT collection on Omnisea", create_omnisea),
            Choice("7) Mint MailZero NFT", mint_mailzero_nft),
            Choice("8) Mint ZKS Domain", mint_zks_domain),
            Choice("9) Send message L2Telegraph", send_message),
            Choice("10) Create gnosis safe", create_safe),
            Choice("11) Use custom routes", custom_routes),
            Choice("12) Exit", "exit"),
        ],
        qmark="⚙️ ",
        pointer="✅ "
    ).ask()
    if result == "exit":
        sys.exit()
    return result

def get_wallets():
    accounts = ACCOUNTS
    if DECRYPT_ACCOUNTS and DECRYPT_ACCOUNTS_PASS:
        accounts = []
        for account in ACCOUNTS:
            try:
                account = decrypt_private_key(account, DECRYPT_ACCOUNTS_PASS)
                accounts.append(account)
            except Exception as e:
                if 'Padding is incorrect' in str(e):
                    print(f'Failed to encrypt: Wrong password')
                    return
                else:
                    print(f'Failed to encrypt account {account}: {str(e)}')

    need_proxy = False
    accs = accounts
    if USE_PROXY or USE_MOBILE_PROXY:
        mob_proxies = []
        if MOBILE_PROXY:
            for i in range(len(accounts)):
                mob_proxies.append(MOBILE_PROXY)

        need_proxy = True
        account_with_proxy = dict(zip(accounts, PROXIES)) if USE_PROXY else dict(zip(accounts, mob_proxies))
        accs = account_with_proxy

    wallets = [
            {
                "id": _id,
                "key": key,
                "proxy": account_with_proxy[key] if need_proxy else None
            } for _id, key in enumerate(accs, start=1)
        ]
    return wallets


async def run_module(module, account_id, key, proxy):
    await module(account_id, key, proxy)


async def main(module):
    wallets = get_wallets()

    if RANDOM_WALLET:
        random.shuffle(wallets)

    for _, account in enumerate(wallets, start=1):
        sleep_time = random.randint(SLEEP_FROM, SLEEP_TO)
        await run_module(module, account["id"], account["key"], account["proxy"])

        if USE_MOBILE_PROXY and CHANGE_PROXY_URL:
            resp = requests.get(CHANGE_PROXY_URL)

            if resp.status_code != 200:
                raise Exception(f'status_code = {resp.status_code}, response = {resp.text}')

        if _ < len(wallets):
            logger.success(f'Delay before next wallet is {sleep_time}')
            await asyncio.sleep(sleep_time)

    logger.success('Finished')


if __name__ == '__main__':
    module = get_module()
    if module == "tx_checker":
        get_tx_count()
    else:
        asyncio.run(main(module))
