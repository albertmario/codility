#!/usr/bin/python

arai = []

def arrayF(n):
	arr = [0] * (n + 1)
	i = 2
	while(i * i <= n):
		if arr[i] == 0:
			j = i * i
			while j <= n:
				if arr[j] == 0:
					arr[j] = i
				j += i
				
		i += 1
	return arr
	
#bagian paling keren ada di bawah fungsi ini
def cek_faktor(n):
	prime = []
	sum = 0
	
	for i in range(len(arai)):
		if arai[i]:
			b = i / arai[i] 
			if arai[b] == 0:
				sum += 1
		prime.append(sum)
	
	return prime
	
def solution(N, P, Q):
	global arai
	arai = arrayF(N)
	
	hasil = []
	arai_lagi = cek_faktor(N)
	for i in range(len(P)):
		
		hasil.append(arai_lagi[Q[i]] - arai_lagi[P[i] - 1])
	
	return hasil

print solution(26,[1,4,16],[26, 10, 20])



