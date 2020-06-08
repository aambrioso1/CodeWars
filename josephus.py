"""
Solving: https://www.codewars.com/kata/josephus-permutation/

def josephus(n,k)

Examples with 
[1,2,3,4,5,6,7] - initial sequence
[1,2,4,5,6,7] => 3 is counted out and goes into the result [3]
[1,2,4,5,7] => 6 is counted out and goes into the result [3,6]
[1,4,5,7] => 2 is counted out and goes into the result [3,6,2]
[1,4,5] => 7 is counted out and goes into the result [3,6,2,7]
[1,4] => 5 is counted out and goes into the result [3,6,2,7,5]
[4] => 1 is counted out and goes into the result [3,6,2,7,5,1]
[] => 4 is counted out and goes into the result [3,6,2,7,5,1,4]

So josephus(7,3) = [3,6,2,7,5,1,4]

Note the the Josephus survivor should sit in position 4.
"""

def josephus(items,k):
	if items == []: # return an empty list if items is empty
		return []
	next = (k - 1) % len(items) # the position of the next item to be removed
	j_perm = [] # initialize the Josephus permuation at empty
	for i in range(len(items) - 1):
		j_perm.append(items.pop(next))  # pops the element at the next position off the items list
		next = (next + k - 1) % len(items) # Many other people used this same idea!
	return j_perm			


l = list('CodeWars')
print(josephus([1,2,3,4,5,6,7,8,9,10],1))
print(josephus([1,2,3,4,5,6,7],3))
print(josephus([1,2,3,4,5,6,7,8,9,10],2))
print(josephus([1,2,3,4,5,6,7,8,9,10],40))
print(josephus(l,4))
print(josephus([],3))
print(josephus([i for i in range(1,42)], 2))
