
from brownie import Lottery, accounts, config, network
from scripts.deploy_lottery import deploy_lottery
from web3 import Web3
import pytest

def test_get_entrance_fee():
        if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
            pytest.skip()
        # Arrange
        lottery = deploy_lottery()
        # Act
        # 2000 eth / usd
        # usdEntryFee = 50
        # entryFee = 2000 / usdEntryFee
        expected_entry_fee = Web3.toWei(0.025, "ether")
        entrance_fee = lottery.getEntranceFee()
        # Assert
        assert expected_entry_fee == entrance_fee