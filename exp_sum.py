"""
Explosive Sum
https://www.codewars.com/kata/52ec24228a515e620b0005ef

https://en.wikipedia.org/wiki/Partition_(number_theory)#

This a classic problem.   I will try to implement it in different ways.
Not too concerned about working it out from scratch.



**** Sample Tests ****
test.describe('testing exp_sum')
test.it('***** Very basic tests *****\n')
test.assert_equals(exp_sum(1), 1)
test.assert_equals(exp_sum(2), 2)
test.assert_equals(exp_sum(3), 3)
test.it('_____ So far so good _____\n')
test.it('\n***** Funcionality tests *****\n')
test.assert_equals(exp_sum(4), 5)
test.assert_equals(exp_sum(5), 7)
test.assert_equals(exp_sum(10), 42)
"""
"""
# This solution came from the Encyclopedia of Integer Sequences: 
# https://oeis.org/A000041
def exp_sum(n):
    if n > 40: break
    if n == 0: return 1
    
    S = 0; J = n-1; k = 2
    
    while 0 <= J:
        T = exp_sum(J)
        S = S+T if (k//2 % 2 == 1) else S-T
        J -= k if k % 2 == 1 else k//2
        k += 1

    return S
"""

# This code found here:  https://stackoverflow.com/questions/7802160/number-of-ways-to-partition-a-number-in-python
def exp_sum(n):
    """Gives the number of ways of writing the integer n as a sum of positive integers,
    where the order of addends is not considered significant.
    """
    dic = {}
    def p(n, k):
        """Gives the number of ways of writing n as a sum of exactly k terms or, equivalently, 
        the number of partitions into parts of which the largest is exactly k.  
        """
        if n < k:
            return 0
        if n == k:
            return 1
        if k == 0:
            return 0
        
        key = str(n) + ',' + str(k)
        try:
            temp = dic[key]
        except:
            temp = p(n-1, k-1) + p(n-k, k)
            dic[key] = temp
        finally:
            return temp
    
    partitions_count = 0
    for k in range(n + 1):    
        partitions_count += p(n, k)
    return partitions_count


print(f'{exp_sum(4)=} should be 5')
print(f'{exp_sum(5)=} should be 7')
print(f'{exp_sum(10)=} should be 42')