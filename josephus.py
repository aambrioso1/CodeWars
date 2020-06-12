"""
This is my solutions to the following CodeWars problem:
	https://www.codewars.com/kata/josephus-permutation/

def josephus(items,k)

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
	
	if items == []: # Return an empty list if items is empty.
		return []
	
	next = (k - 1) #  % len(items)  The position of the next item to be removed.
	j_perm = [] # Initialize the Josephus permuation at empty.
	
	for i in range(len(items) - 1):
		j_perm.append(items.pop(next))  # Pops the element at the next position off the items list.
		# Once I solved it, I was able to see other solutions.   There were a few super clever one-liners. 
		# But many people used the same idea that I did.  The next line is the key idea. 
		# The next item to be remove will be the kth one from the item just removed.
		# First we add k to next.   Since the list is one item shorter after the pop, we need to subtract 1.
		# Since that addition may result in a number greater that the length of the list, we do the calculation
		# mod the length of the list.   This brings the next point back around to the beginning of the list.
		next = (next + k - 1) % len(items)
	
	return j_perm			

l = list('CodeWars') # a list of the letters in CodeWars.

print(josephus([1,2,3,4,5,6,7,8,9,10],1))
print(josephus([1,2,3,4,5,6,7],3))
print(josephus([1,2,3,4,5,6,7,8,9,10],2))
print(josephus([1,2,3,4,5,6,7,8,9,10],40)) # test for k greater than the size of the items.
print(josephus(l,4)) # tests a list of strings.
print(josephus([],3)) # tests an empty list.
print(josephus([i for i in range(1,42)], 2)) # This is the original problem with 41 soldiers.  The survivor is 19.