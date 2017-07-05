#!/usr/bin/python

def solution(A, B, K):
	
	A_mod = A % K
	
	if A_mod:
		A += (K - A_mod)
	
	B -= B % K
	
	return (B - A) / K + 1
	
print solution(6,8,2)
