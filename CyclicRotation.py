#!/usr/bin/python

def solution(A, K):
	panjang = len(A)
	hasil = [0]*panjang
	
	for i in range(panjang):
		temp = i + K
		hasil[temp % panjang] = A[i]
	
	return hasil

print solution([1,2,3,4,5], 3)
