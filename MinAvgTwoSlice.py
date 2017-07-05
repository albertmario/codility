#!/usr/bin/python

def solution(A):
	minim = None
	for i in range(len(A)):
		awal = A[i]
		count = 1
		Q = i + 1
		if i == len(A) - 1:
			break
			
		while 1:
			tempAvg = sum(A[i:Q + count])*1.0 / len(A[i:Q + count])
	
			if minim == None:
				minim = tempAvg
				pos = i
				
			if tempAvg < minim:
				minim = tempAvg
				pos = i
			
			if count == 2:
				break
				
			count += 1
	
	return pos
			
print solution([10000,-10000])
