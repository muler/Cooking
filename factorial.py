import math
from itertools import permutations
def get_factorials(n):
	return_list = []
	for x in range(n):
		return_list.append(math.factorial(n))
	return return_list
def get_permutations(n):
	cols = range(n)
	count = 0
	for vec in permutations(cols):
		if(n == len(set(vec[i]+i for i in cols))==len(set(vec[i]-i for i in cols))):
			#print vec
			count = count +1
	
	           		
factorn = get_factorials(10)
get_permutations(10)
#print factorn

