#!/usr/bin/python

def solution(A):
	if len(A) == 0:
		return 0
		
	kecil = None
	besar = None
	temp = []
	
	for i in A:
		if kecil == None:
			kecil = i
		if i >= kecil:
			temp.append(i - kecil)
		if i < kecil:
			kecil = i
	
	return max(temp)
	
print solution([0,200])
