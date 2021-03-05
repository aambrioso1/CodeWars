"""
URL for Befunge in CodeWars:  https://www.codewars.com/kata/526c7b931666d07889000a3c/train/python

Instructions for Befunge Interpreter

0-9 Push this number onto the stack.

+ Addition: Pop a and b, then push a+b.
- Subtraction: Pop a and b, then push b-a.
* Multiplication: Pop a and b, then push a*b.
/ Integer division: Pop a and b, then push b/a, rounded down. If a is zero, push zero.
% Modulo: Pop a and b, then push the b%a. If a is zero, push zero.
! Logical NOT: Pop a value. If the value is zero, push 1; otherwise, push zero.
*********** Start here ********************************************************************
` (backtick) Greater than: Pop a and b, then push 1 if b>a, otherwise push zero.
> Start moving right.
< Start moving left.
^ Start moving up.
v Start moving down.
? Start moving in a random cardinal direction.
_ Pop a value; move right if value = 0, left otherwise.
| Pop a value; move down if value = 0, up otherwise.
" Start string mode: push each character's ASCII value all the way up to the next ".
: Duplicate value on top of the stack. If there is nothing on top of the stack, push a 0.
\ Swap two values on top of the stack. If there is only one value, pretend there is an extra 0 on bottom of the stack.
$ Pop value from the stack and discard it.
. Pop value and output as an integer.
, Pop value and output the ASCII character represented by the integer code that is stored in the value.
# Trampoline: Skip next cell.
p A "put" call (a way to store a value for later use). Pop y, x and v, then change the character at the position (x,y) in the program to the character with ASCII value v.
g A "get" call (a way to retrieve data in storage). Pop y and x, then push ASCII value of the character at that position in the program.
@ End program.
(i.e. a space) No-op. Does nothing.
The above list is slightly modified: you'll notice if you look at the Wikipedia page that we do not use the user input instructions and dividing by zero simply yields zero.

Here's an example:

>987v>.v
v456<  :
>321 ^ _@

will create the output 123456789.

So what you must do is create a function such that when you pass in the Befunge code, the function returns the output that would be generated by the code. So, for example:

"123456789".equals(new BefungeInterpreter().interpret(">987v>.v\nv456<  :\n>321 ^ _@")
This test case will be added for you.

"""

"""
***********
* Imports *
***********
"""
from collections import deque
from random import randint


"""
******************
* Initialization *
******************
"""
# The program, the stack and the output are global variables for now.
program1 = '>987v>.v\nv456<  :\n>321 ^ _@'
program2 = '>123456789'
pointer = (0,0) # Tuple points to current location in the program string : (row, column)
# Docs for collections.deque
# https://docs.python.org/3/library/collections.html#collections.deque
 # The direction tuple shows current direction: (right, left).  For example (1,0) is right and
 # (0,-1) is down.
 
direction = (1, 0)

stack = deque() # The stack
output = [] # The output.   A list might not be the right data type for the output.

"""
********************
* Helper functions *
********************
"""
def pop():

	a = stack.pop()
	if a != '':
		return 0
	return output.append(a)

"""
**********************
* Befunge operations *
**********************
"""

def push(e): 
	# 0-9 Push this number onto the stack.
	stack.append(e)

# Binary operations

def add():
	# + Addition: Pop a and b, then push a+b.
	b = stack.pop()
	a = stack.pop()
	c = a + b
	push(c)

def subtract():
	# - Subtraction: Pop a and b, then push b-a.
	a = stack.pop()
	b = stack.pop()
	c = b - a
	push(c)

def multiply():
	# * Multiplication: Pop a and b, then push a*b.
	b = stack.pop()
	a = stack.pop()
	c = a * b
	push(c)

def divide():
	# / Integer division: Pop a and b, then push b/a, rounded down. If a is zero, push zero.
	b = stack.pop()
	a = stack.pop()
	if a == 0:
		push(0)
	else:
		c = b // a
		push(c)

def mod():
	# % Modulo: Pop a and b, then push the b%a. If a is zero, push zero.
	b = stack.pop()
	a = stack.pop()
	if a == 0:
		push(0)
	else:
		c = b % a
		push(c)

def log_not():
	# ! Logical NOT: Pop a value. If the value is zero, push 1; otherwise, push zero.
	a = stack.pop()
	if a != 0:
		push(1)
	else:
		push(0)

def greater_than():
	pass

def right():
	pass

def left():
	pass

def up():
	pass

def down():
	pass

"""
***********************
* Experimental output *
***********************
"""
"""
for c in program1:
	if c == '\n':
		print(f'newline {c}')
	else: 
		print(f'not newline: {c}')
"""

# Testing push and the binary operators
# Push
push(1)
push(2)
push(3)
push(4)
push(5)
push(6)
push(7)
push(8)
push(9)
print(f'Initial stack = {stack}')

# Binary operators
add()
print(f'After add, stack = {stack}')
subtract()
print(f'After subtract, stack = {stack}')
multiply()
print(f'After multiply, stack = {stack}')
divide()
print(f'After divide, stack = {stack}')
mod()
print(f'After mod, stack = {stack}')
log_not()
print(f'After log_not, stack = {stack}')

push(1)

print(f'After push(1), stack = {stack}')