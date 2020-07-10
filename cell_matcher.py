"""
Given two squares on a chess board using standard chess notation, a1 (lower left) to h8 (upper right), the funcion
cell_matcher(cell1, cell2) returns true if the squares are the same color and false if they are not.
This solve the CodeWars problem:  https://www.codewars.com/kata/5894134c8afa3618c9000146
Note the code will need some minor tweaking to solve the problem.   I leave that to reader.
"""

# We use zip to create a dictionary.
d = dict(zip('abcdefgh',range(8)))

def cell_matcher(cell1, cell2):
	# We assign a number to each cell based on its coordinates.
	# Note the use of unpacking and multiple assignment here.
	x1, y1 = cell1
	x2, y2 = cell2
	sum1 = d[x1] + int(y1) # sum of the first cells coordinates.
	sum2 = d[x2] + int(y2) # sum of the second cells coordinates.
	
	# We decide if cell match color in a simple mathematical way.
	if sum1 % 2 == sum % 2:
		return True
	return False

#  This function allows us to put some nice language into our output automatically.
def answer(b):
	if b:
		return 'are'
	return "are not"

c1, c2 = 'a1', 'a2'  # This pair of squares are not the same color.
ans = answer(cell_matcher(c1,c2))
print(f'The cells {c1} and {c2} {ans} the same color.')  # Note how simple it is too use f strings to produce nicely formatted output.

c1, c2 = 'a1', 'b2' # This pair of squares are the same color.
ans = answer(cell_matcher(c1,c2))
print(f'The cells {c1} and {c2} {ans} the same color.')