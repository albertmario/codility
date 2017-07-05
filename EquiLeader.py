#!/usr/bin/python

def find_leader(A):
	size = 0
	value = None
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
		return count, value
	else:
		return -1

def solution(A):
	count = 0
	temp = None
	kiri = 0
	
	if find_leader(A) == -1:
		return 0
	else:
		kanan, value = find_leader(A)
	
	for i in range(len(A)):
		if A[i] == value:
			kiri += 1
			kanan -= 1
		
		if (kiri > (i + 1) / 2) and (kanan > (len(A) - i - 1) / 2):
			count += 1
	
	return count
		
print solution([4,3,4,4,4,2])
