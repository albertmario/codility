#!/usr/bin/python

import math

def solution(A):
	arr = [0] * (max(A) + 1)
	for i in A:
		arr[i] += 1

	hasil = []
	
	for i in range(len(A)):
		temp = 0
		for j in range(1, int(math.sqrt(A[i])) + 1 ):
			if A[i] % j == 0:
				temp += arr[j]
				if A[i] / j != j:
					temp += arr[A[i] / j]
					
		hasil.append(len(A) - temp)
	
	return hasil
	
print solution([3,1,2,3,6])
