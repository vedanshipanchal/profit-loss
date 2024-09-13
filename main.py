actualprice = 100
sellprice = 200
#formuls
profit = sellprice - actualprice
loss = actualprice - sellprice
#conditions
if(sellprice>actualprice):
 print("the profit is",profit)
else:
   print("the loss is",loss)