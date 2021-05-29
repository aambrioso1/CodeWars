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

def exp_sum(n):
    if n == 0: return 1
    
    S = 0; J = n-1; k = 2
    
    while 0 <= J:
        T = exp_sum(J)
        S = S+T if is_odd(k//2) else S-T
        J -= k if is_odd(k) else k//2
        k += 1

    return S

print(f'{exp_sum(4)=} should be 5')
print(f'{exp_sum(5)=} should be 7')
print(f'{exp_sum(10)=} should be 42')