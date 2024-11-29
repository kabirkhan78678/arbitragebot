from web3 import Web3

# Connect to an Ethereum node using Infura (replace with your own Infura API key)
infura_url = "https://mainnet.infura.io/v3/c1f5fb0a3b3146adbfef7293d5129979"
web3 = Web3(Web3.HTTPProvider(infura_url))

# SushiSwap Router contract address
sushiswap_router_address = "0xd9e1cE17f2641f24aE83637ab66a2cca9C378B9F"

# SUSHI token contract address
sushi_token_address = "0x6b3595068778dd592e39a122f4f5a5cf09c90fe2"

def get_token_price():
    # Load contract ABIs
    with open("uniswap_abi.json", "r") as abi_file:
        uniswap_abi = abi_file.read()

    # Instantiate contract objects
    sushiswap_router = web3.eth.contract(address=web3.to_checksum_address(sushiswap_router_address), abi=uniswap_abi)
    sushi_token = web3.eth.contract(address=web3.to_checksum_address(sushi_token_address), abi=uniswap_abi)

    # Get reserves
    reserves = sushiswap_router.functions.getReserves(sushi_token_address, web3.eth.default_account).call()

    # Assuming the token has two reserves (token0 and token1), you can calculate the price
    token0_reserve, token1_reserve = reserves
    token_price = token1_reserve / token0_reserve
    
    return token_price

if __name__ == "__main__":
    price = get_token_price()
    print(f"SUSHI Token Price: {price} ETH")
