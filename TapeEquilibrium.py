#!/usr/bin/python

def solution(A):
	kiri = 0
	kanan = sum(A)
	minim = None

	for i in range(len(A) - 1):
		kiri += A[i]
		kanan -= A[i]
		temp = abs(kiri - kanan)
		
		if minim == None:
			minim = temp
		else:
			minim = min(minim, temp)
	
	return minim

print solution([-2,-2])
