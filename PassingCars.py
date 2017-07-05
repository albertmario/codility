#!/usr/bin/python

def solution(A):
	east = 0
	count = 0
	
	for i in A:
		if i == 0:
			east += 1
		else:
			count += east
	
	return count
				

print solution([0,0,1])
