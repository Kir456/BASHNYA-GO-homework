from math import pow
t = int(input())
res = []

for j in range(t):
    n = int(input())

    operations = {}
    ind = 0
    while n != 0:
        if n % 3 != 0:
            operations[ind] = n % 3
        n //= 3
        ind += 1

    cost = 0
    for i in operations:
        price = int(pow(3, i+1)+i*pow(3, i-1))*operations[i]
        cost += price
    
    res.append(cost)

for j in range(t):
    print(res[j])