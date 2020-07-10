import math

def A006257(n):

     return 0 if n==0 else 2*(n-2**int(math.log(n, 2)))+1 # Indranil Ghosh, Jan 11

print(A006257(41))