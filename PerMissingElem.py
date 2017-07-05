#!/usr/bin/python

def Solution(A):
	if not A:
		return 1
		
	A = sorted(A)
	temp = 1
	
	for i in A:
		if i != temp:
			return temp
		temp += 1
		
	return A[-1] + 1
	

print Solution([1])
