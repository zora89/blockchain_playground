from web3 import Web3
import json

infura_url = "https://mainnet.infura.io/v3/a31f23202f1f44568b85e40d13814ac2"
web3 = Web3(Web3.HTTPProvider(infura_url))

#testing for True connection state with eth blockchain
print(web3.isConnected())

#fetching for latest eth blockd data and saving to latest_block variable
latest_block = web3.eth.get_block('latest')

#Will print all info regarding latest eth block
print(latest_block)
print(web3.eth.blockNumber)

#corerction for lower case eth addresses, you are welcome to donate eth to the funds below :) 
adress_correction = Web3.toChecksumAddress('0x10F94d0C2C14Ff9C244940760CA0bd2dc445fDB3')

#acquiring a specific wallet balance
balance = web3.eth.getBalance(adress_correction)

print(balance)
#web3.fromWei -> helps covert Wei balance to required currency(positional argument)
print(web3.fromWei(balance, 'ether'))
