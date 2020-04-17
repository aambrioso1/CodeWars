def asterisc_it(n): 
    if isinstance(n, int):
        s = str(n)
    elif isinstance(n, list):
        s = ''
        for i in n:
            s += str(i)
    else:
        s = n
    ct = 0
    ans = ''
    while(ct < len(s)-1):
        d1 = int(s[ct])
        d2 = int(s[ct+1])
        if d1 % 2 == 0 and d2 % 2 == 0:
            ans += s[ct] +'*'
            ct += 1
        else:
            ans += s[ct]
            ct += 1
    ans += s[ct]
    return(ans)
