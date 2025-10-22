t = int(input())
res = []

for u in range(t):
    k = int(input())

    if k <= 9:
        res.append((1+k)*k//2)
        continue

    s = 9
    i = 1
    while s <= k:
        i += 1
        s += i*9*10**(i-1)
    
    s -= i*9*10**(i-1)
    ost = k-s
    i -= 1
    
    count = 0
    for j in range(1, 10):
        count += j*i*10**(i-1)
    
    dl = ost//(i+1)
    last = ost%(i+1)
    if last != 0:
        num = str(10**i+dl)
        for q in range(last):
            count += int(num[q])
    
    if dl == 0:
        res.append(count)
        continue

    last_num = str(dl+10**i-1)
    plus = 0
    for w in range(i):
        plus += int(last_num[w])
    count += plus+int(last_num[-1])
    for x in range(i, -1, -1):
        start = 0
        if x == 0:
            start = 1
        for y in range(start, int(last_num[x])):
            if x != i:
                count += (plus+y)*10**(i-x)+45*(i-x)*10**(i-x-1)
            else:
                count += (plus+y)*10**(i-x)
        if x != 0:
            plus -= int(last_num[x-1])
    
    res.append(count)

for i in range(t):
    print(res[i])