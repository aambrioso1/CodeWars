def halving_sum(n):
    sum = n
    half = n
    while(half//2 >= 1):
        print(half)
        half = half//2
        sum += half
    return sum
