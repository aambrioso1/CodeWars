import math
from functools import lru_cache

@lru_cache(maxsize=None)
def josephus_survivor2(n,k):
	# This follow the recursion given in the nice article in Wikipedia:  https://en.wikipedia.org/wiki/Josephus_problem
	if k == 1:
		return n - 1
	if n == 1:
		return 0
	if 1 < n < k:
		return (josephus_survivor2(n-1, k) + k) % n
	if k <= n:
		n_pr = n - math.floor(n / k)
		return math.floor(k*((josephus_survivor2(n_pr,k) - (n % k)) % n_pr) / (k - 1))

@lru_cache(maxsize=None)
def josephus_survivor(n,k):
	# A simple way to adjust for the fact that the recursive function in the article using positions from 0 to n - 1,
	# while the CodeWars problem is based on positions from 1 to n.
	return 1 + josephus_survivor2(n,k)

print(josephus_survivor(7,3))
print(josephus_survivor(11,19))
print(josephus_survivor(1,300))
print(josephus_survivor(14,2))
print(josephus_survivor(100,99))
