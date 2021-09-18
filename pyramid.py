# pyramid.py

# https://www.codewars.com/kata/515f51d438015969f7000013/python

# My Solution
def pyramid(n):
    list = []
    for i in range(0,n):
        list.append([1 for _ in range(i+1)])
    return list




"""
Nice solution contributed by CodeWars competitors
sahglie, Cptnprice, amarovita, Maciek57, mugunth, radq, conor-mullen, flocurity, ilinovster, Afkor (plus 47 more warriors)
"""

def pyramid(n):
    return [[1]*x for x in range(1, n+1)]
