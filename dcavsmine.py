import csv
#from distutils.command.build_scripts import first_line_re 
import os 
import json
from traceback import print_tb



def percent_in_change():
    def chang(price1, price2):
        return (price2 - price1) / price2   

    ds = []
    chs = [0,]
    prcs = []
    with open('btcdaily.csv', 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            ds.append(row[0])
            prcs.append(float(row[1]))
        for i,z in zip(prcs, prcs[1:]):
            #print(i,z)
            num = chang(i,z) * 100
            print()
            chs.append(float(f'{num:.3f}'))
    with open('btcdailych.csv', 'a+') as fi:
        csvwriter = csv.writer(fi)
        for chg, dss, prc in zip(chs, ds, prcs):

            csvwriter.writerow([dss, prc, chg])
#percent_in_change()





#print(f"{a = :.3f}, {b = :.3f}, { c= :.3f}")
#chang()
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
    if amount < 0:
        print(False)
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


with open('ada-now.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        # 1 date
        # 2 price 
        # 3 change
        prices.append(float(row[1]))
        datetimes.append(row[0])
        changes.append(float(row[2]))
        
first_price_dca = 11.23
first_price_20 = 11.23
first_price_25 = 11.23
first_price_30 = 11.23
first_price_35 = 11.23
first_price_40 = 11.23
first_price_45 = 11.23
first_price_50 = 11.23

for price, change in zip(prices, changes):
    #pass
    dca_shit += dca(price, first_price_dca)
    #print(change > 0)
    mine_shit_20 += mine(price, change,first_price_20, 50, change > 0)
    #mine_shit_25 += mine(price, change,first_price_25, 25, change > 0)
    #mine_shit_30 += mine(price, change,first_price_30, 30, change > 0)
    #mine_shit_35 += mine(price, change,first_price_35, 35, change > 0)
    #mine_shit_40 += mine(price, change,first_price_40, 40, change > 0)
    #mine_shit_45 += mine(price, change,first_price_45, 45, change > 0)
    #mine_shit_50 += mine(price, change,first_price_50, 100, change > 0)
#for i in changes:
#    print(i > 0, i)
now_price = 45814.50
#print(dca_shit * now_price
#,mine_shit_20 * now_price
#,mine_shit_25 * now_price
#,mine_shit_30 * now_price
#,mine_shit_35 * now_price
#,mine_shit_40 * now_price
#,mine_shit_45 * now_price
#,mine_shit_50 * now_price, 10*365 )
##print(shit)
print()
