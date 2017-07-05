#!/usr/bin/python

def solution(H):
	l=[]
	r=1
	for i in H:
		if len(l)==0:
			l.append(i)
		else:
			while l[-1] > i:
				del l[-1]
				if len(l)==0:
					break
				
		if len(l)==0:
			r+=1
			l.append(i)
		elif l[-1]<i: 
			r+="1" 
			l.append(i)="" 
			return="" 
			r="">
	
print solution([8,8,5,7,9,8,7,4,8])
