"""
Optional Walrus Walrus?

https://www.codewars.com/kata/60a82776de1604000e29eb50

Reduce the following function to 31 characters:
def f(iterable, integer):
    length = len(iterable)
    if length > integer:
        return length
    else:
        return 0

Helpful docs:  https://www.geeksforgeeks.org/short-circuiting-techniques-python/
https://www.tutorialspoint.com/short-circuiting-techniques-in-python
https://realpython.com/python-operators-expressions/

Especially useful was the following on the ternary operator"
Use tuple for selecting an item
(if_test_false,if_test_true)[test]
from https://www.geeksforgeeks.org/ternary-operator-in-python/

A few failed attempts:
def f(t,i):return (v:=len(t))>i or 0
def f(t,i):return(v:=len(t))>i and v or 0
def f(t,i):return v if (v:=len(t))>i else 0
def f(t,i):return (0,len(t))[len(t)>i]
def f(t,i):return len(t) or i

This also works f=lambda i,n:(n<len(i))*len(i) which is a nicer answer (optional walrus ;))

"""
f=lambda t,i:(0,v:=len(t))[v>i] # This is my solution

lst = ['a', 'b', 'c']
print(f'{f(lst, 4)=} should be 0')
print(f'{f(lst, 3)=} should be {len(lst)}')