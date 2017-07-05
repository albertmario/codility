#!/usr/bin/python

def solution(N, A):
	arr_hasil = [0] * N
	besar = 0
	bantu = 0
	
	for i in A:
		if i <= N:
			if arr_hasil[i - 1] < besar:
				arr_hasil[i - 1] = besar
				
			arr_hasil[i - 1] += 1
			bantu = max(arr_hasil[i - 1], bantu)
			
		else:
			besar = max(bantu, besar)
	
	for i in range(len(arr_hasil)):
		arr_hasil[i] = max(besar, arr_hasil[i])
		
	return arr_hasil
	
print solution(5,[3,4,4,6,1,4,4])
