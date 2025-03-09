# implement a program that: 
#    Expects the user to specify as a command-line argument the number of Bitcoins,n, that they
#     would like to buy.   If that argument cannot be converted to a float,
#     the program should exit via sys.exit with an error message. 
#    Queries the API for the CoinCap Bitcoin Price Index at https://api.coincap.io/v2/assets/bitcoin 
#     which returns a JSON object,  among whose nested keys is the current price of Bitcoin as a float.
#     Be sure to catch any exceptions, as with code
#       import requests
#       try: 
#           ... 
#       except requests.RequestException: 
#           ... 
#    Outputs the current cost of Bitcoins in USD to four decimal places, using , as a thousands
#      separator. 
# 
# I will need to install the 'requests' package, the 'JSON' package is native to Python. 
#            py -m pip install requests

import requests
import sys

def main():
    # print(f"len(sys.argv) is {len(sys.argv)}")
    # for cmd line 'py bitcoin.py cat',
    #  len(sys.argv) is 2

    try:
        if len(sys.argv) != 2:
            sys.exit("Missing command-line argument")
        else:
            coins_to_buy = float(sys.argv[1])
            print(f"coins to buy is {coins_to_buy}")

            response = requests.get('https://api.coincap.io/v2/assets/bitcoin')
            content = response.json()
            #print(f"data key has value {content["data"]}")
            usd_coin_price = float(content["data"]["priceUsd"])
            print(f"usd_coin_price is {usd_coin_price}")
            amount = coins_to_buy * usd_coin_price
            print(f"${amount:,.4f}")


#         print(content)
# #       {'data':
# #       {'id': 'bitcoin',
# #        'rank': '1',
# #        'symbol': 'BTC',
# #        'name': 'Bitcoin',
# #        'supply': '19834446.0000000000000000',
# #        'maxSupply': '21000000.0000000000000000',
# #        'marketCapUsd': '1658395281602.7769484664299850',
# #        'volumeUsd24Hr': '5441717221.7261839322256531',
# #        'priceUsd': '83611.8781236832603475',
# #        'changePercent24Hr': '-3.1499479823409685',
# #        'vwap24Hr': '85353.0232204382325462',
# #        'explorer': 'https://blockchain.info/'},
# #        'timestamp': 1741533678183}        
    except requests.HTTPError:
        print("Could not make request")
    except requests.RequestException:
        print("Request exception")
    except ValueError:
        sys.exit("Command-line argument is not a number")


main()



