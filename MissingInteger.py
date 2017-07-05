#!/usr/bin/python

def solution(A):
	A = sorted(list(set(A)))
	hasil = []
	for i in A:
		if i > 0:
			hasil.append(i)

	print hasil
	if not hasil:
		return 1
		
	i = 1
	
	while 1:
		if hasil[i - 1] != i:
			return i
		i += 1
		if i > len(hasil):
			break
	
	return max(hasil) + 1
			
print solution([-2147483648,-2147483647])
