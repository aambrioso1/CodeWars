#  Took me a while to figure this one out.
#  Three cheers to Ada Lovelace!!!

from fractions import Fraction
from math import factorial

# It was two slow to pass with my math function.
"""
def fact(n):
    # Computes n!
    prod = 1
    for i in range(n):
        prod *= i + 1
    return prod
"""
def comb(n,r):
    # Computes the bionomial coefficients
    return factorial(n) // (factorial(r) * factorial(n - r))
    
def bernoulli_number(n):
    if n % 2 == 1 and n >= 3:
        return 0
    # Define some convenient fractions
    zero = Fraction(0,1)
    one = Fraction(1,1)
    neg_one = Fraction(-1,1)
    
    b_list = [one]
    c_list = [[comb(i,j) for j in range(i)] for i in range(2,n+2)]

    for seq in c_list:
        if len(b_list) % 2 == 1 and len(b_list) >= 4:
            b_list.append(zero)
        else:
            sum = 0
            for i in range(len(seq)-1):

                sum += b_list[i]*seq[i]
                new_b = Fraction(neg_one*sum,seq[len(seq)-1])
            b_list.append(new_b)
    # print(b_list)
    return b_list[n]
