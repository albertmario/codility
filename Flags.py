#!/usr/bin/python

import math

def solution(A):
	peaks = []
	
	for i in range(1, len(A) - 1):
		if A[i - 1]< A[i] and A[i] > A[i + 1]:
			peaks.append(i)
	
	if len(peaks) <= 2:
		return len(peaks)
	
	hasil = 0
	
	for i in range(3, int(math.sqrt(peaks[-1] - peaks[0]) + 2)):
		flags = 1
		tanda = peaks[0]
		for j in range(1, len(peaks)):
			if abs(peaks[j] - tanda) >= i:
				flags += 1
				tanda = peaks[j]
			
			if flags == i:
				hasil = max(hasil, flags)
				break
	
	return hasil
				
print solution([0, 0, 0, 0, 0, 1, 0, 1, 0, 1])
