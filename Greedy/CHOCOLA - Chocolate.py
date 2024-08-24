t = int(input())
for _ in range(t):
    input()
    m, n = list(map(int, input().split()))
    m, n = m - 1, n - 1
    x, y = [], []
    for _ in range(m):
        x.append(int(input()))
    for _ in range(n):
        y.append(int(input()))
    
    x.sort(reverse=True)
    y.sort(reverse=True)

    horizontal, vertical = 1, 1
    i , j = 0, 0
    res = 0
    while i < m and j < n:
        if x[i] > y[j]:
            res += x[i] * vertical
            horizontal += 1
            i += 1
        else:
            res += y[j] * horizontal
            vertical += 1
            j += 1
    
    while i < m:
        res += x[i] * vertical
        i += 1
    
    while j < n:
        res += y[j] * horizontal
        j += 1
    print(res)
