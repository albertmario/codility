#!/usr/bin/python

def solution(A):
	arr_cek = [0 for i in range(len(A))]
	count = 0
	
	for i in range(len(A)):
		
		try:
			if arr_cek[A[i] - 1] < 1:
				count += 1
				arr_cek[A[i] - 1] += 1
			else:
				return 0
		except:
			return 0
		
		if count == len(A):
			return 1
		
	if count < len(A):
		return 0
		
print solution([2])
