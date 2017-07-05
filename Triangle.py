#!/usr/bin/python

def solution(A):
	A = sorted(A)
	A = A[::-1]
	
	for i in range(len(A) - 2):
		if A[i] + A[i + 1] > A[i + 2] and A[i] + A[i + 2] > A[i + 1] and A[i + 2] + A[i + 1] > A[i]:
			return 1
	
	return 0
	
print solution([10,50,55,1])
		
