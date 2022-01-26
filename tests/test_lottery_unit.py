
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account
from brownie import Lottery, accounts, config, network, exceptions
from scripts.deploy_lottery import deploy_lottery
from web3 import Web3
import pytest

from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS
# import pytest

def test_get_entrance_fee():
        if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
                pytest.skip("This test is only for local blockchain environments")
        # Arrange
        lottery = deploy_lottery()
        # Act
        # 2,000 eth / usd
        # usdEntryFee = 50
        # 2000/1 == 50/x == 0.025
        expected_entrance_fee = Web3.toWei(0.025, "ether")
        entrance_fee = lottery.getEntranceFee()
        # Assert
        assert expected_entrance_fee == entrance_fee

def test_cant_enter_unless_started():
        if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
                pytest.skip()
        lottery = deploy_lottery()
        with pytest.raises(exceptions.VirtualMachineError):
                lottery.enter({"from": get_account(), "value": lottery.getEntranceFee()})

def test_can_start_and_enter_lottery():
        if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
                pytest.skip()
        lottery = deploy_lottery()
        account = get_account()
        lottery.startLottery({"from": account})
        lottery.enter({"from": account, "value": lottery.getEntranceFee()})
        assert lottery.players(0) == account