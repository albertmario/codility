#!/usr/bin/python

def solution(A,B):
	turun = []
	naik = 0
	size = None
	
	for i in range(len(A)):
		if B[i] == 0:
			naik += 1
			
			while 1:
				if len(turun) == 0:
					break
					
				if A[i] > turun[-1]:
					del(turun[-1])
				else:
					naik -=1
					break
		else:
			turun.append(A[i])
	
	return len(turun) + naik

print solution([4,3,2,1,5],[1,1,1,0,0])
