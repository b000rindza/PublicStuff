import numpy as np


matches = []

for i in range(0, 3):
	for j in range(i+1, 4):
		matches.append([i ,j])

print(matches)




def base3(n):
	
	
	digit_pow = 5 # good for representing 3^(digit_pow+1) values
	digits = []
	
	while (n>=0):
		
		digit = n // (3**digit_pow)
		if (digit_pow==0):
			digit = n
		
		digits.append(digit)		
		n -= digit * (3**digit_pow)
			
		
		#print(digit_pow, digits, n)		
		
		if (n==0) and (digit_pow==0):
			#print("base3 finished")
			break
		
		digit_pow -= 1
		
		if (n<0) or (digit_pow<0):
			print("base3 failed")
			break
		
		
	
	return digits

print("TEST - base3")
print(base3(1))
print(base3(3))
print(base3(65))
print(base3(728))
print("\n\n")


# We have 6 matches, each with 3-3 inpendent outcomes
# The index of a list can represent which match we refer to, and the stored value can represent the outcome
# This is equivalent to having a 6-digit number in base3
# We just have to iterate through every "number" and compute what the outcomes amount to
# input    : 6 digit base3 number 
# output : the scores of the players




def calcScore(outcomes): # 6-digit base3 number
	
	scores = [0, 0, 0, 0]
	
	for i in range(len(matches)):
		a, b = matches[i]
		outcome = outcomes[i]
		
		if outcome == 0: # tie, everyone gets 1 point
			scores[a] += 1
			scores[b] += 1
		if outcome == 1: # 1st player wins and gets 3 point
			scores[a] += 3
		if outcome == 2: #2nd player wins and gets 3 points
			scores[b] += 3
		
	return scores
		


print(calcScore([0, 1, 1, 2, 0, 2])) # output : 7, 2, 3, 4
print(matches) #[[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]
#0: 1 + 3 + 3
#1: 1 + 1
#2: 3 
#3: 1 + 3
print("\n\n")


scores = []

for i in range(729):
	print(i)
	scoreBuffer = calcScore(base3(i))
	#print(scoreBuffer)
	scoreBuffer.sort(reverse=True)
	#print(scoreBuffer)
	scores.append( scoreBuffer )
#print("len : ", len(scores))


scoreSet = set()
for s in scores:
	setBuffer = ''.join(str(x) for x in s)
	scoreSet.add(setBuffer)

print(scoreSet)

scoreList = list(scoreSet)
scoreList.sort()
print(scoreList)
print("len : ", len(scoreList))

