t = int(input())
res = []

for i in range(t):
    n = int(input())

    arr = []
    count = 0
    j = 1
    while True:
        delit = 1+10**j
        if delit > n:
            break
        if n % delit == 0:
            count += 1
            arr.append(n//delit)
        j += 1
    
    res.append(str(count))
    if count != 0:
        arr = sorted(arr)
        res.append(' '.join(map(str, arr)))

print('\n'.join(f'{x}' for x in res))