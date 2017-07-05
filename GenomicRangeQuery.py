#!/usr/bin/python

def solution(S, P, Q):
	arr_DNA = []
	
	for i in S:
		arr_DNA.append([0,0,0,0])
	
	for i in range(len(S)):
		if S[i] == 'A':
			arr_DNA[i][0] += 1
		elif S[i] == 'C':
			arr_DNA[i][1] += 1
		elif S[i] == 'G' :
			arr_DNA[i][2] += 1
		else:
			arr_DNA[i][3] += 1
			
		try:
			arr_DNA[i + 1] = arr_DNA[i][:]
		except:
			pass		
		
	hasil = []

	for i in range(len(P)):
			
		if arr_DNA[Q[i]][0] > arr_DNA[P[i]][0] or S[P[i]] == 'A':
			hasil.append(1)
		elif arr_DNA[Q[i]][1] > arr_DNA[P[i]][1]  or S[P[i]] == 'C':
			hasil.append(2)
		elif arr_DNA[Q[i]][2] > arr_DNA[P[i]][2]  or S[P[i]] == 'G':
			hasil.append(3)
		else:
			hasil.append(4)
		
	return hasil
	
print solution('AC', [0,0,1], [0,1,1]) 
