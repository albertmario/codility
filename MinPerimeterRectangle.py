#!/usr/bin/python

import math

def solution(N):
	hasil = []
	
	for i in range(1, int(math.sqrt(N)) + 1):
		if N % i == 0:
			luas = 2 * (i + N/i)
			hasil.append(luas)
				
	return min(hasil)
	
print solution(30)
