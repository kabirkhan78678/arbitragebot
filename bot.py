import requests

def get_algorand_markets():
    # CoinGecko API endpoint for Algorand
    url = 'https://api.coingecko.com/api/v3/coins/algorand/markets'

    try:
        # Make the API request
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            algorand_markets = response.json()

            # Print the market data or process it as needed
            for market in algorand_markets:
                print(f"Exchange: {market['name']}")
                print(f"Pair: {market['pair']}")
                print(f"Volume: {market['volume']}")
                print(f"Price: {market['current_price']}")
                print("-----")

        else:
            print(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    get_algorand_markets()
