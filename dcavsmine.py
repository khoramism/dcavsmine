import csv
from distutils.command.build_scripts import first_line_re 
import os 
import json 

def dca(price, amount):
    return amount / price 

dca_shit = 0
#K = [20,25,30,35,40,45,50]
def mine(price, change, amount , K, p_or_n):
    #p_or_n = True if change >= 0 else False
    if p_or_n:
        amount = amount - (change* K/100)
    else:
        amount = amount - (change* K/100)
    #elif change == 0:
    #    amount = amount
    # the amount bought 
    print(amount)
    global first_price
    first_price = amount
    return amount / price 
    

prices = []
datetimes = []

changes = []
mine_shit_20 = 0
mine_shit_25 = 0
mine_shit_30 = 0
mine_shit_35 = 0
mine_shit_40 = 0
mine_shit_45 = 0
mine_shit_50 = 0


with open('btcss.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        # 1 date
        # 2 price 
        # 3 change
        prices.append(float(row[1]))
        datetimes.append(row[0])
        changes.append(float(row[2]))
        
first_price_dca = 10
first_price_20 = 10
first_price_25 = 10
first_price_30 = 10
first_price_35 = 10
first_price_40 = 10
first_price_45 = 10
first_price_50 = 10

for price, change in zip(prices, changes):
    dca_shit += dca(price, first_price_dca)
    #print(change > 0)
    mine_shit_20 += mine(price, change,first_price_20, 50, change > 0)
    #mine_shit_25 += mine(price, change,first_price_25, 25, change > 0)
    #mine_shit_30 += mine(price, change,first_price_30, 30, change > 0)
    #mine_shit_35 += mine(price, change,first_price_35, 35, change > 0)
    #mine_shit_40 += mine(price, change,first_price_40, 40, change > 0)
    #mine_shit_45 += mine(price, change,first_price_45, 45, change > 0)
    #mine_shit_50 += mine(price, change,first_price_50, 50, change > 0)
#for i in changes:
#    print(i > 0, i)
#print(dca_shit * 50663
#,mine_shit_20 * 50663
#,mine_shit_25 * 50663
#,mine_shit_30 * 50663
#,mine_shit_35 * 50663
#,mine_shit_40 * 50663
#,mine_shit_45 * 50663
#,mine_shit_50 * 50663,530)
#print(shit)
