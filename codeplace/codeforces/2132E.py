t = int(input())
res = []

for _ in range(t):
    n, m, q = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort(reverse=True)
    b.sort(reverse=True)
    for i in range(q):
        test = list(map(int, input().split()))

        