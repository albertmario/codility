#!/usr/bin/python

import math

def solution(X, Y, D):
	return int(math.ceil((Y - X)*1.0 / D))

print solution(10,85,30)
