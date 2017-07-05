#!/usr/bin/python

a = int(raw_input())
hasil = []

while 1:
	hasil.append(a%2)
	a /= 2
	if a == 0:
		break

hasil.reverse()

jawab = []
buka = 0
masuk = 0
count = 0

for i in hasil:
	if buka == 1:
		if i == 0:
			count += 1
			masuk = 1
		if i == 1:
			if masuk == 1:
				jawab.append(count)
				count = 0
				masuk = 0
	else:
		if i == 1:
			buka = 1
	

try:
	print max(jawab)
except:
	print 0

