d = {0: [], 1: [], 2: [], 3: []}

def stem_and_leaf(data):
    d = dict(zip(range(10),[[] for i in range(10)]))
    for n in data:
        d[n//10].append(n % 10)
    print(d)
    for i in range(10):
        if d[i] == []:
            d.pop(i)
    for key in d.keys():
        d[key].sort()
    return d