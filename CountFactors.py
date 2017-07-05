#!/usr/bin/python

import math

def solution(N):
	count = 0
	for i in range(1, int(math.sqrt(N)) + 1):
		if N % i == 0:
			if N / i == i:
				count += 1
			else:
				count += 2
	
	return count
	
print solution(25)
