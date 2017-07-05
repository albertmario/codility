#!/usr/bin/python

def solution(A):
	atas = sorted([i + radius for i, radius in enumerate(A)])
	bawah = sorted([i - radius for i, radius in enumerate(A)])
	
	hasil = 0
	j = 0
	
	for i, nilai in enumerate(atas):
		while j < len(atas) and nilai >= bawah[j]:
			hasil += j - i
			j += 1
		if hasil > 10**7:
			return -1
	
	return hasil

print solution([1,5,2,1,4,0])
			
