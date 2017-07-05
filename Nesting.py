#!/usr/bin/python

def solution(S):
	stack = []
	kiri = ['{', '[', '(']
	kanan = ['}', ']', ')']
	
	for i in S:
		if i in kiri:
			stack.append(i)
		elif i in kanan:
			if len(stack) == 0:
				stack.append(i)
			else:
				if (stack[-1] == '{' and i == '}') or (stack[-1] == '[' and i == ']') or (stack[-1] == '(' and i == ')'):
					del(stack[-1])
				else:
					stack.append(i)

	if len(stack):
		return 0
	else:
		return 1

print solution('())')
