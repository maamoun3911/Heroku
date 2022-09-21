import requests
# import time

APIKey = '74ba0d3e-ab8e-46ee-9285-5c5ca9342e76'
BotAPIToken = '5518808804:AAGGqq-Oh8LA0acf1st6AyI_oHCMagK65_U'
chat_id = '772715406'
limit = 59000
# time_intervel = 5

def get_price():
    url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    
    parameters = {
        'start':'1',
        'limit':'1',
        'convert':'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '74ba0d3e-ab8e-46ee-9285-5c5ca9342e76',
    }

    response = requests.get(url, headers=headers, params=parameters).json()
    Currency_price = response['data'][1]['quote']['USD']['price']
    return Currency_price
# print(get_price())

def send_update(chat_id, msg):
    url = f"https://api.telegram.org/bot{BotAPIToken}/sendMessage?chat_id={chat_id}&text={msg}"
    requests.get(url)

    # chat_id, text

def main_fun():
    # while True:
    i = 0
    while i < 1:
        price = get_price()
        if price < limit:
            send_update(chat_id, f"بقولك ايه يا مأمون سعر البيتكوين{price}")
        i += 1
        # time.sleep(time_intervel)
main_fun()
