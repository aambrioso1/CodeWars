def primes(n):
    prime_list = [2]
    for val in range(1, n + 1): 
        if val > 1:
            for i in range(2, val//2 + 2): 
                if (val % i) == 0:
                    break
                else:
                    if i == val//2 + 1:
                        prime_list.append(val)
    return prime_list

prime_list = primes(5000)

def total(arr):
    sum = 0
    for i, num in enumerate(arr):
        if i in prime_list:
            sum += num
    return sum