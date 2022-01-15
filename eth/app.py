from web3 import Web3
infura_url = "https://mainnet.infura.io/v3/a31f23202f1f44568b85e40d13814ac2"
web3 = Web3(Web3.HTTPProvider(infura_url))
print(web3.isConnected())
latest_block = web3.eth.get_block('latest')
#print(latest_block)
balance_zp = web3.eth.getBalance("0x10F94d0C2C14Ff9C244940760CA0bd2dc445fDB3")
print(web3.fromWei(balance_zp, 'ether'))