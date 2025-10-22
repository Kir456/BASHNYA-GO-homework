t = int(input())
res = []

for i in range(t):
    n = int(input())
    a = str(input())
    m = int(input())
    b = str(input())
    c = str(input())

    for j in range(m):
        if c[j] == 'D':
            a = a + b[j]
        elif c[j] == 'V':
            a = b[j] + a
    
    res.append(a)

for i in range(t):
    print(res[i])