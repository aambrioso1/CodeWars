# A program that generates a triangle of numbers to illustrate the triangle numbers.
# For information on the triangular numbers see https://en.wikipedia.org/wiki/Triangular_number.
# Alex Ambrioso Spring 2020

"""
def blanks(n):
    # Prints n blank spaces
    return n * '*'

def print_num(m,n):
    # Prints a string from n to m with each integer separated by a single space.
    # For example print_num(1,3) returns '1 2 3 '
    st = ''
    for i in range(m,n+1):
        if i == n:
            st += str(i)
        else:
            st += str(i) + '*'
    return st

def points(n):
    # Calculates the number of points in the nth triangular number
    return n * (n - 1) // 2

def triangle(n):
    # Creates a triangle of consecutive integers for each triangular number
    for i in range(1,n+1):
        print(f'{blanks(n-i)}' + print_num(points(i)+1, points(i) + i))

# Prints out the first ten triangles
for k in range(1,11):
    print(f'Here is a triangle for n = {k}')
    triangle(k)
    print('')

n = points(5)
string = ''

for i in range(1,6):
    string += blanks(i) + "\n"

print(string)
"""


# The problem that the format of triangle does not work when combined with str_tri and my method inserting.    The trianle
# needs to be in the from of the final output string for insertion recursion to work.
def triangle(in_string, n, d, start): 
    #  Creates a triangle of digits
    # in_string is a string of strings with n rows each containing a string of n charactors
    # A list of blanks list to create an array
    # a = [[] for i in range(n)] 
    a = in_string
    x, y = start
    # a = [['' for i in range(n)] for j in range(n)] 
    # print(a)
    # These nested loops generate the pattern of numbers bounding the triangle
    for i in range(n):
        for j in range(n):
            # Generates the right of the triangle of digits
            if i == j:
                a[i+x][j+y] = str((i+d) % 10)
            # Generates the bottom of the triangle of digits
            if i == n - 1:
                for j in range(n-1):
                #a[i] = [str(((2*n-1)-i) % 10) for i in range(n)]
                    a[i+x][j+y] = str((((2*n-2)-j)+d) % 10)
            # Generates the left side of the triangle of digits
            if 0 < i < n - 1 and j == 0:
                a[i+x][j+y] = str((((3*n-3)-i)+d) % 10)
    return a

n = 8
my_string1 = [['' for j in range(n)] for k in range(n)] 
tri1 = triangle(my_string1, n, 0, (0,0))


n = 5
# my_string2 = [['' for j in range(n)] for k in range(n)] 
tri2 = triangle(tri1, n, 0, (2,1))

print('tri2', tri2)

# The empty string string is built up to create the triangular pattern of digits we desire.

def string_tri(arr, k):
    string = ''
    
    for i, list in enumerate(arr):
        string += ((k - i) * ' ') + ' '.join(list) + '\n'
    return string  

# string1 = string_tri(my_string1, 8)
string2 = string_tri(tri2, 8)

# print('tri1', tri1)
# print(string1)
print('*********')
print(tri2)
print(string2)

""""
n = 8

# my_string = [['' for j in range(n)] for k in range(n)] 
tri = triangle(tri, n, 0)

# The empty string string is built up to create the triangular pattern of digits we desire.

def string_tri(arr):
    string = ''
    
    for i, list in enumerate(tri):
        string += ((n - i) * ' ') + ' '.join(list) + '\n'
    return string  
string = string_tri(tri)

print(string)
"""



"""

# We generate ten triangles
for i in range(10):
    my_string = [['' for j in range(i)] for k in range(i)] 
    print(triangle(my_string, i,5))
"""