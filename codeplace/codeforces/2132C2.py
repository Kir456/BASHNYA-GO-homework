from math import pow
t = int(input())
res = []

for j in range(t):
    n, k = list(map(int, input().split()))

    operations = {}
    ind = 0
    count = 0
    inds = []
    while n != 0:
        ost = n % 3
        if ost != 0:
            operations[ind] = ost
            count += ost
            inds.append(ind)
        n //= 3
        ind += 1
    
    if count > k:
        res.append(-1)
        continue
    
    if count > k-2:
        cost = 0
        for i in operations:
            price = int(pow(3, i+1)+i*pow(3, i-1))*operations[i]
            cost += price
        res.append(cost)
        continue

    x = (k-count)//2
    while x > 0:
        curr_ind = inds[-1]
        if curr_ind == 0:
            break
        num = operations[curr_ind]
        if num <= x:
            del operations[curr_ind]
            inds.pop()
            inds.append(curr_ind-1)
            if curr_ind-1 in operations:
                operations[curr_ind-1] += 3*num
            else:
                operations[curr_ind-1] = 3*num
            x -= num
        elif num > x:
            operations[curr_ind] -= x
            if curr_ind-1 in operations:
                operations[curr_ind-1] += 3*x
            else:
                operations[curr_ind-1] = 3*x
            break
    
    cost = 0
    for i in operations:
        price = int(pow(3, i+1)+i*pow(3, i-1))*operations[i]
        cost += price
    res.append(cost)

for j in range(t):
    print(res[j])