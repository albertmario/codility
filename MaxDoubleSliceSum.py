#!/usr/bin/python

def solution(A):
	kiri = [0]
	kanan = []
	temp = 0
	
	for i in range(1,len(A) - 2):
		temp = max(0, temp + A[i])
		kiri.append(temp)
	
	A = A[::-1]
	temp = 0
	for i in range(1, len(A) - 2):
		temp = max(0, temp + A[i])
		kanan.append(temp)
	
	kanan = kanan[::-1]
	kanan.append(0)
	temp = 0

	for i in range(len(kiri)):
		temp = max(temp, kiri[i] + kanan[i])
	
	return temp
print solution([3,2,6,-1,4,5,-1,2])
