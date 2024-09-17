# given 2 sorted arrays, get the max sum by traversing them, you can jump to other array only when you find a common element in both arrays.
def solve(a1, a2):
    freq = {}
    n, m = len(a1), len(a2)
    i ,j = 0, 0
    while i < n and j < m:
        if a1[i] == a2[j]:
            freq[i] = j
            i += 1
            j += 1
        elif a1[i] < a2[j]:
            i += 1
        else:
            j += 1
    s1, s2 = [], []
    i ,j = 0, 0
    for k,v in freq.items():
        s1.append(a1[i:k+1])
        s2.append(a2[j:v+1])
        i = k + 1
        j = v + 1
    s1.append(a1[i:n+1])
    s2.append(a1[j:m+1])
    res = 0
    for i in range(len(s1)):
        res += max(sum(s1[i]), sum(s2[i]))
    return res
    
ans = solve([1, 3, 7, 8, 10], [1, 4, 6, 7, 9])
print(ans)