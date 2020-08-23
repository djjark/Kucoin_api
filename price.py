# price calculator

print("preco de compra:")
buy_price = float(input())
print("preco de venda:")
sell_price = float(input())
print("quantidade:")
quantity = float(input())

quantity = quantity / buy_price
print(quantity)
s = buy_price*quantity
s1 = s-(s*0.001)
b = sell_price*quantity
b1 = b-(b*0.001)
tr = b-s
tb = (b*0.001+s*0.001)
print("lucro: "+str(tr-tb)+" taxa: "+str(tb))

