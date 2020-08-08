import json
from datetime import datetime
from kucoin.client import Client
import numpy as np
with open('C:/Users/Diogo/Desktop/codes.json') as f:
  data = json.load(f)

API_passphrase= data['API_passphrase']
trading_password= data['trading_password']
secret_api_pass=  data['secret_api_pass']
api_key= data['api_key']     

client = Client(api_key,secret_api_pass,API_passphrase)

currency = "AMPL"
quantity = 40

order = client.get_order_book('AMPL-USDT')
buys = order['asks']


def date(var):
    return datetime.utcfromtimestamp(int(var)).strftime('%Y-%m-%d %H:%M:%S')

# tempo reals
# print(datetime.utcfromtimestamp(  int(time in unixtimestamp)  ).strftime('%Y-%m-%d %H:%M:%S'))

# integrate.simps(sells)

# counter=1
# while(1):
#     balance_ETH=""
#     balance_USDT=""
#     for i in client.get_accounts():
#         if i["currency"]==currency:
#             balance_currency=i["balance"]
#         elif i["currency"]=="USDT":
#             balance_USDT = i["balance"]

#     var = int(client.get_timestamp()/1000)
#     ts = client.get_kline_data('AMPL-USDT', '1min',var-80)
#     print(ts)
#     print(date(var))
#     if ts:
#         price_point = float(ts[0][2])
#         print(ts[0][2])
#     price_low = price_point - 0.01
#     price_high = price_point + 0.01
#     balance_currency = float(balance_currency)
#     if counter<1 and balance_currency>1:
#         order = client.create_limit_order('AMPL-USDT', Client.SIDE_SELL, price_high, quantity, time_in_force='GTT', cancel_after=5)
#         counter+=1
#     else:
#         if counter<1:
#                                                 # moeda, compra / venda, preco, quantidade de moeda
#             order = client.create_limit_order('AMPL-USDT', Client.SIDE_BUY, price_low, quantity, time_in_force='GTT', cancel_after=5)
#             counter+=1
#     # se nao houver ordens activas
#     if not(client.get_orders("AMPL-USDT","active")["items"]):
#         counter-=1
#     print("")

