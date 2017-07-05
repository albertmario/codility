#!/usr/bin/python

def gcd(a, b):
	if a % b == 0:
		return b
	else:
		return gcd(b, a % b)
		
		
def solution(A, B):
	hasil = 0
	
	for i in range(len(A)):
		bantu = gcd(A[i], B[i])
		
		c = 0
		while c != 1:
			c = gcd(A[i], bantu)
			A[i] /= c
		
		c = 0
		while c!= 1:
			c = gcd(B[i], bantu)
			B[i] /= c
		
		if A[i] == 1 and B[i] == 1:
			hasil += 1
	
	return hasil
	
print solution([15, 10, 3], [75, 30, 5])
