import json
from datetime import datetime
from kucoin.client import Client
from kucoin.exceptions import KucoinAPIException
import numpy as np
import time
from make_Calculations import make_Calculations

with open('D:/TensorFlow/GitHub projects/Kucoin/codes.json') as f:
  data = json.load(f)

trading_password= data['trading_password']
client = Client(data['api_key'] ,data['secret_api_pass'],data['API_passphrase'])

AMPL_account="5f2340b16ce385000791808e"
ETH_account="5c6a49fb99a1d819392efda9"

def calculate_amount():
    for i in client.get_accounts():
        if i['currency'] == 'USDT':
            return float(i['available'])
        
coin="AMPL"
pair="ETH"
pairs= [f"{coin}-USDT", f"{coin}-{pair}", f"{pair}-USDT"]
quantity = calculate_amount() # USDT
variance = 0.01

    
    
def date(var):
    return datetime.utcfromtimestamp(int(var)).strftime('%Y-%m-%d %H:%M:%S')


# FAZER O S = COM 2 CASAS DECIMAIS
#  este esta certo e funciona
def USDT_AMPL_ETH_USDT(a, b, c):
    s = str(round(quantity/a, 2)) # FAZER COM 2 CASAS DECIMAIS
    order = client.create_limit_order(str(pairs[0]), Client.SIDE_BUY, a, size=s) # quantidade da moeda a comprar
    
    while(client.get_order(order['orderId'])['isActive'] == True):
        continue
    qq = float(client.get_order(order['orderId'])['size']) - float(client.get_order(order['orderId'])['fee'])
    qq = str(round(qq, 2))
    order1 = client.create_limit_order(pairs[1], Client.SIDE_SELL, b, qq)
    while(client.get_order(order1['orderId'])['isActive'] == True):
        continue
    qq1 = float(client.get_order(order1['orderId'])['size']) - float(client.get_order(order1['orderId'])['fee'])
    qq1 = str(round(qq1*b, 5))
    order2 = client.create_limit_order(pairs[2], Client.SIDE_SELL, c, qq1)
    print("Completed")


def USDT_ETH_AMPL_USDT(a, b, c):
    s = str(round(quantity/c,5))
    order = client.create_limit_order(pairs[2], Client.SIDE_BUY, c, size=s)
    while(client.get_order(order['orderId'])['isActive'] == True):
        continue
    qq = float(client.get_order(order['orderId'])['size']) - float(client.get_order(order['orderId'])['fee'])
    qq = str(round(qq/b,2))    
    order1 = client.create_limit_order(pairs[1], Client.SIDE_BUY, b, qq)
    while(client.get_order(order1['orderId'])['isActive'] == True):
        continue
    qq1 = float(client.get_order(order1['orderId'])['size']) - float(client.get_order(order1['orderId'])['fee'])
    qq1 = str(round(qq1, 2))
    order2 = client.create_limit_order(pairs[0], Client.SIDE_SELL, a, qq1)
    print("Completed")



def prints(x, var, swag, swag1,a,b,c):
    print(date(var-460))
    print("balance: "+str(quantity))
    print(str(round(swag,5))+f" {coin}-USDT > {coin}-{pair}")
    
    print(str(round(swag1,5))+f" {coin}-USDT < {coin}-{pair}")
    vr = b * c
    print(f"{coin}-USDT: "+str(a)+f" {coin}-{pair}: "+str(b*c)+f" {pair}-USDT: "+str(c))
    
def sell_buy_sell(quantidade):
    var = int(client.get_timestamp()/1000)
    verify_AMPL_USDT = float(client.get_kline_data(pairs[0], '1min', var-1560)[0][2])
    verify_AMPL_ETH = float(client.get_kline_data(pairs[1], '1min', var-1560)[0][2])
    verify_ETH_USDT = float(client.get_kline_data(pairs[2], '1min', var-1560)[0][2])
    x = make_Calculations(quantidade, verify_AMPL_USDT, verify_AMPL_ETH, verify_ETH_USDT)
    swag = x.calc_USDT_ETH_AMPL_USDT()
    swag1 = x.calc_USDT_AMPL_ETH_USDT()
    prints(x, var, swag, swag1, verify_AMPL_USDT, verify_AMPL_ETH, verify_ETH_USDT)
    # Retirar de comentario para funcionar com o reverse
    try:
        if(swag > variance):
            USDT_ETH_AMPL_USDT(verify_AMPL_USDT, verify_AMPL_ETH, verify_ETH_USDT)
        elif(swag1 > variance):
            USDT_AMPL_ETH_USDT(verify_AMPL_USDT, verify_AMPL_ETH, verify_ETH_USDT)
    except KucoinAPIException as e:
        pass

    
    
while(1):
    sell_buy_sell(quantity)


def get_coins(market1, market2):
    sw = client.get_symbols()
    tt = len(sw)
    USDT = []
    ETH = []
    for i in range(tt):
        k=sw[i]['symbol']
        # print(len(k))
        l=""
        for j in range(len(k)-4,len(k)):
            l+=k[j]
        if l==market1:
            USDT.append(sw[i]['symbol'])
        if l==f"-{market2}":
            ETH.append(sw[i]['symbol'])

    last=[]
    for i in USDT:
        for j in ETH:
            if i[0] == j[0] and i[1] == j[1] and i[2] == j[2]:
                last.append(i)
    print(last)

# get_coins("USDT", "ETH")
# tempo reals
# print(datetime.utcfromtimestamp(  int(time in unixtimestamp)  ).strftime('%Y-%m-%d %H:%M:%S'))

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
