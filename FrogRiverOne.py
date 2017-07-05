#!/usr/bin/python

def solution(X, A):
	arr_cek = [0 for i in range(1, X + 1)]
	i = 0
	count = 0
	
	while 1:
		print count
		if A[i] <= X:
			if arr_cek[A[i] - 1] == 0:
				arr_cek[A[i] - 1] = A[i]
				count += 1
		
		if count == X:
			return i
			
		i += 1
		if i == len(A):
			break
	
	return -1
	
print solution(3, [1,3,5,3,5,2])
