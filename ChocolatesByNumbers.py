#!/usr/bin/python

def gcd(N, M):
	if N % M == 0:
		return M
	else:
		return gcd(M, N % M)

def solution(N, M):
	pembagi = gcd(N, M)
	return N / pembagi

print solution(15,75)
