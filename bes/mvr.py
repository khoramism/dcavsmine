import csv 
import os

file = open('DONE.csv', 'r') 
file2 = open('Res.csv', 'r')

filew = open('DONE-LAST.csv', 'a+') 
filew2 = open('Res11111.csv', 'a+')

fr = csv.reader(file)
res = csv.reader(file2)

fw1 = csv.writer(filew)
fw2 = csv.writer(filew2)





def cp_please(fn):
	print(fn)
	os.system(f'scp -r  hashtag@178.63.240.70:/home/hashtag/source/multimedia/custtel/mamad/{fn} .')

#for i in fr:
#	cp_please(i[0])

aud1 = []

shit = []

aud2 = []

shit2 = []
ksaks = []


def finds(fn):
	if fn[0] in shit2:
		num = shit2.index(fn[0])
		fw1.writerow([shit2[num], shit2[num + 1], fn[1]])



for i in fr:
	aud1.append(i[0])
	shit.append([i[0], i[1]])
	#aud2.append(z)

for z in res:
	aud2.append(z[0])
	shit2.append(z[0])
	shit2.append(z[1])


#for i in res:
#	fw2.writerow([i[0]])

for qw in shit:
	#print(qw)
	finds(qw)

print(len(ksaks))	