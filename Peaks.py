#!/usr/bin/python

def solution(A):
	peaks = []
	
	for i in range(1, len(A) - 1):
		if A[i - 1]< A[i] and A[i] > A[i + 1]:
			peaks.append(i)
	
	if len(peaks)== 0:
		return 0
		
	hasil = 0
	for i in range(1, len(A)):
		if len(A) % i == 0:
			block = len(A) / i
			x = 0
			for j in peaks:
				if (j >= block * x) and (j < block * (x + 1)):
					x += 1
			
			if x == i:
				hasil = i
			
			
	return hasil
	
print solution([1,2,3,4,3,4,1,2,3,4,6, 2])
