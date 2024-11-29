import requests
import json
import csv

def get_algorand_info():
    # Define the API endpoint URL for Algorand
    url = "https://api.coingecko.com/api/v3/coins/algorand?market_data=true"

    try:
        # Make a GET request to the API
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            algorand_data = response.json()

            # Extract relevant information
            general_info = {
                "name": algorand_data['name'],
                "symbol": algorand_data['symbol'],
                "current_price_usd": algorand_data['market_data']['current_price']['usd']
            }

            markets_info = []

            for market in algorand_data['tickers']:
                market_info = {
                    "exchange": market['market']['name'],
                    "pair": f"{market['base']}/{market['target']}",
                    "last_price": market['last'],
                    "volume": market['volume'],
                    "trust_score": market['trust_score'],
                    "bid_ask_spread_percentage": market['bid_ask_spread_percentage'],
                    "timestamp": market['timestamp'],
                    "trade_url": market['trade_url']
                }
                markets_info.append(market_info)

            # Create the final response
            api_response = {
                "general_info": general_info,
                "markets_info": markets_info
            }

            # Save the information to a CSV file
            with open('algorand_info.csv', 'w', newline='') as csvfile:
                fieldnames = ['exchange', 'pair', 'last_price', 'volume', 'trust_score', 'bid_ask_spread_percentage', 'timestamp', 'trade_url']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                # Write header
                writer.writeheader()

                # Write data
                for market_info in markets_info:
                    writer.writerow(market_info)

            print("CSV file 'algorand_info.csv' has been created.")
        else:
            print(f"Error: Unable to fetch data. Status code: {response.status_code}")

    except Exception as e:
        print(f"Error: {e}")

# Call the function to get Algorand information
get_algorand_info()
