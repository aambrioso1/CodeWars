"""
Your task, is to create a NxN spiral with a given size.

For example, spiral with size 5 should look like this:

00000
....0
000.0
0...0
00000
and with the size 10:

0000000000
.........0
00000000.0
0......0.0
0.0000.0.0
0.0..0.0.0
0.0....0.0
0.000000.0
0........0
0000000000
Return value should contain array of arrays, of 0 and 1, for example for given size 5 result should be:

[[1,1,1,1,1],[0,0,0,0,1],[1,1,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Because of the edge-cases for tiny spirals, the size will be at least 5.

General rule-of-a-thumb is, that the snake made with '1' cannot touch to itself.

"""
def spiralize(size):
    # Make a snake
    return spiral

def square_array(size):
	arr = []
	for i in range(size):
		arr.append([0 for i in range(size)])
	return arr

def loop(arr):
	size = len(arr[0])
	for i in [0, size - 1]:
		for j in range(size):
			arr[i][j] = 1
	for i in range(size):
		arr[i][size - 1] = 1
	return arr

size = 5

spiral = square_array(size)

print('spiral', loop(spiral))

