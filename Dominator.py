#!/usr/bin/python

def solution(A):
	size = 0
	
	for i in A:
		if size == 0:
			value = i
			size += 1
		else:
			if value != i:
				size -= 1
			else:
				size += 1
	
	count = 0
	for i in range(len(A)):
		if A[i] == value:
			count += 1
		if count > len(A) / 2:
			return i
	return -1
		
print solution([6,5,6,4,6,7,3])
