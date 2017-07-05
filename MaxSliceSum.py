#!/usr/bin/python

def solution(A):
	temp = 0
	max_slice = A[0]
	
	for i in A:
		temp = max(i,temp + i)
		max_slice = max(temp, max_slice)
			
	return max_slice

print solution([-4,-5,-1,-2,2,-8,-9])
