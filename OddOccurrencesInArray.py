#!/usr/bin/python

'''
You have to think of the integers in their binary format. By applying the XOR function of the running result to every element in the array, the binary versions of these integers end up "cancelling each other out" because the first XOR flips certain bits, and by applying XOR again with the same integer later on, you end up flipping them back. What you are left with is the one integer that never cancelled itself out.
'''

def solution(arr):
	hasil = 0
	for i in arr:
		hasil ^= i
	return hasil
	

print solution([5,2,2,5,5,5])
