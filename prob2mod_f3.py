#!/usr/bin/env python

import numpy as np
import scipy
from scipy import special



def comb(n, k): # n chose k - "n alatt a k"
	return scipy.special.factorial(n)/(scipy.special.factorial(n-k)*scipy.special.factorial(k))


def P_sum(p, n, s): # the probability of n s-sided dices giving a sum of p
# Source : https://www.omnicalculator.com/statistics/dice

	res = 0
	for k in np.linspace(0, np.floor((p-n)/s).astype(int), np.floor((p-n)/s).astype(int)+1):
		#print(k)
		res += (-1)**k * comb(n, k) * comb(p-s*k-1, n-1)
	
	return (1/s**n)*res


print("Example :")
print("The Probability of throwing a Sum of 30 with 7 6-sided dice) :", P_sum(30, 7, 6))
print("\n")


# A throws with 7 dice
# B throws with 9 dice
# What is the probabilty of A throwing a strictly larger sum than B?

# Solution :
# The probability of A throwing a number D with 7 dice is given by the formula P(D, n, s) above
# Similarly, we can calculate the probabily of B throwing 9, ..., D-1
# Therefore, if we iterate through all the possible sums A can throw that also provide the opportunity for B to throw a smaller number (namely 10, ..., 42)
# The completeness of the probabilty : A throws D*(B throws greater + B throws equal + B throws smaller)
# We only need the last term


Aprobs = []
for D in range (10, 43): # A throws 10 to 42
	Aprobs.append(P_sum(D, 7, 6))

Bprobs = []
for K in range(9,42): # B throws 9 to 41
	Bprobs.append(P_sum(K, 9, 6))


res = 0
for A in range(0, len(Aprobs)):
	buff = 0
	for B in range(0, A+1):
		buff += Bprobs[B]
	res += Aprobs[A]*buff

print("The probability of player B throwing a smaller sum than A throws with 7 dice :\n\t" + str(np.round(res,4)*100)+"%\n")
