from typing import Union, Dict

from loguru import logger
from web3 import Web3
from config import REACTORFUSION_CONTRACTS, REACTORFUSION_ABI
from utils.gas_checker import check_gas
from utils.helpers import retry
from utils.sleeping import sleep
from .account import Account


class ReactorFusion(Account):
    def __init__(self, account_id: int, private_key: str, proxy: Union[None, str]) -> None:
        super().__init__(account_id=account_id, private_key=private_key, proxy=proxy, chain="zksync")

        self.contract = self.get_contract(REACTORFUSION_CONTRACTS["landing"], REACTORFUSION_ABI)

    async def get_tx_data(self) -> Dict:
        tx = {
            "chainId": await self.w3.eth.chain_id,
            "from": self.address,
            "gasPrice": await self.w3.eth.gas_price,
            "nonce": await self.w3.eth.get_transaction_count(self.address),
        }

        return tx

    async def get_deposit_amount(self):
        logger.info(f"Ip address for 'Get deposit amount' is {self.ip}")
        amount = await self.contract.functions.balanceOf(self.address).call()
        return amount

    @retry
    @check_gas
    async def deposit(
            self,
            min_amount: float,
            max_amount: float,
            decimal: int,
            sleep_from: int,
            sleep_to: int,
            make_withdraw: bool,
            all_amount: bool,
            min_percent: int,
            max_percent: int
    ):
        amount_wei, amount, balance = await self.get_amount(
            "ETH",
            min_amount,
            max_amount,
            decimal,
            all_amount,
            min_percent,
            max_percent
        )
        logger.info(f"Ip address for 'Make deposit on ReactorFusion' is {self.ip}")
        logger.info(f"[{self.account_id}][{self.address}] Make deposit on ReactorFusion | {amount} ETH")

        tx_data = await self.get_tx_data()
        tx_data.update({"value": amount_wei})

        transaction = await self.contract.functions.mint().build_transaction(tx_data)

        signed_txn = await self.sign(transaction)

        txn_hash = await self.send_raw_transaction(signed_txn)

        await self.wait_until_tx_finished(txn_hash.hex())

        if make_withdraw:
            await sleep(sleep_from, sleep_to)

            await self.withdraw()

    @retry
    @check_gas
    async def withdraw(self):
        amount = await self.get_deposit_amount()

        if amount > 0:
            logger.info(f"Ip address for 'Make withdraw from ReactorFusion' is {self.ip}")
            logger.info(
                f"[{self.account_id}][{self.address}] Make withdraw from ReactorFusion | " +
                f"{Web3.from_wei(amount, 'ether')} ETH"
            )

            tx_data = await self.get_tx_data()
            tx_data.update({"value": 0, "nonce": await self.w3.eth.get_transaction_count(self.address)})

            transaction = await self.contract.functions.redeem(amount).build_transaction(tx_data)

            signed_txn = await self.sign(transaction)

            txn_hash = await self.send_raw_transaction(signed_txn)

            await self.wait_until_tx_finished(txn_hash.hex())
        else:
            logger.error(f"[{self.account_id}][{self.address}] Deposit not found")
