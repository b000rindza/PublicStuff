#!/usr/bin/env python

import numpy as np



# Generate data (H)
# H is the set of 6-long 0-1 series that contain exactly 3 1-s


H = []
for i in range(4):
	for j in range(i+1, 5):
		for k in range(j+1, 6):
			buff = [0 for x in range(6)]
			buff[i] = 1
			buff[j] = 1
			buff[k] =1
			#print(buff)
			H.append(buff)
			
print("\n\tGENERATED DATA\n")
for i in range(20):
	print(i, H[i], "\n")





# Hamming-distance

def Hamming(a, b):
#	print(a,b)
	if len(a) != len(b):
		print("iterable lengths not equal")
		return 0

	ham = 0
	for i in range(len(a)):
		if a[i] != b[i]:
			ham+= 1

	return ham






# Finding the maximum size of the set of series in which the elements have a larger Hamming-distance than 2

# Solution :
# Assuming there is a maximum size, M>2, we can find if by the following method. First creating 2-sized groups (pairs) and see which elements meet the criteria, then look for a 3rd element for each match. If M=6, we would certainly find it.




# A dict that stores the n-sized groups
pairDict = {}

# Generate the first layer of data
# Storing entire lists uses too much memory, so we store their indeces in H
groupBuffer = []

boolMat =[ [False for x in range(len(H))] for x in range(len(H))]
boolMat[len(H)-1][len(H)-1] = True


for h in range(len(H)-1):
	boolMat[h][h] = True
	
	for i in range(h+1, len(H)):
		#print(h, i)
		if Hamming(H[h], H[i]) > 2:
			groupBuffer.append([h, i])
			boolMat[h][i] = True
			boolMat[i][h] = True

pairDict[2] = groupBuffer

# 0 1 0 1 0 0 1
# 1 0 0 1 0 0 1
# 0 0 0 0 0 0 0
# 1 1 0 0 0 0 1
# 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0
# 1 1 0 1 0 0 0


# 1 1 1 1 0 1 1 . . . 
# 1 1 0 1 0 0 1
# 1 0 1 0 0 0 0
# 1 1 0 1 0 0 1
# 0 0 0 0 1 0 0
# 1 0 0 0 0 1 0
# 1 1 0 1 0 0 1
# ...                   ...


print("\n\tPAIRS\n")
print(pairDict)
print(len(pairDict[2]))
print("\n\tOVERLAP MATRIX\n")
for row in boolMat:
	strBuff = ""
	for elem in row:
		strBuff += str(elem) + "\t"
	print(strBuff)
print("\n\n\nresults....\n\n")



def overlapOne(row_inds, mat):
	
	N = len(mat[0])
	
	res = []
	
	for i in range(max(row_inds)+1, N): # checking if the listed rows overlap at greater indeces
		
		match = True
		for r in row_inds:
			if mat[r][i] == False:
				match = False
				break
		if match:
			res.append(i)
	

	
	return res







for n in range(3, 20+1):
	
	groupBuffer = [] # storing the n-sized groups

	for group in pairDict[n-1]: # iterating through ever n-1 sized group
		
#		groupBuffer = []
		res = overlapOne(group, boolMat) # finding which other element also match the n-1 sized group
		
		for r in res:
			buff = group.copy()
			buff.append(r)
			groupBuffer.append(buff) # generating the n sized group
			#print(groupBuffer[-1])
	#print("groupBuffer", groupBuffer)
	
	
	pairDict[n] = groupBuffer
	print("dict["+str(n)+"] length : ", len(pairDict[n]))
	print(pairDict[n][0:10])









print(pairDict)



res = 0
for p in range(2,len(pairDict)):
	if pairDict[p+1] != []:
		res = p+1


print("\n\nThe largest group found : "+str(res)+"\n")







