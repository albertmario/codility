#!/usr/bin/python

def solution(A):
	A = list(set(A))
	return len(A)

print solution([2,1,1,2,3,1])
