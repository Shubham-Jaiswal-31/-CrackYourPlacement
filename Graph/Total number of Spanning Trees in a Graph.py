MAX = 100
MOD = 1000000007

def multiply(A, B, C):
    for i in range(MAX):
        for j in range(MAX):
            C[i][j] = 0
            for k in range(MAX):
                C[i][j] = (C[i][j] + (A[i][k] * B[k][j]) % MOD) % MOD

def power(A, N, result):
    temp = [[0] * MAX for i in range(MAX)]
    for i in range(MAX):
        for j in range(MAX):
            result[i][j] = 1 if i == j else 0
    while N > 0:
        if N % 2 == 1:
            multiply(A, result, temp)
            for i in range(MAX):
                for j in range(MAX):
                    result[i][j] = temp[i][j]
        N = N // 2
        multiply(A, A, temp)
        for i in range(MAX):
            for j in range(MAX):
                A[i][j] = temp[i][j]

def numOfSpanningTree(graph, V):
    result = [[0] * MAX for i in range(MAX)]
    temp = [[0] * MAX for i in range(MAX)]

    for i in range(V):
        for j in range(V):
            temp[i][j] = graph[i][j]

    power(temp, V - 2, result)
    ans = 0

    for i in range(V):
        for j in range(V):
            ans = (ans + result[i][j]) % MOD
    return ans

if __name__ == "__main__":
    V = 4
    E = 5 
    graph = [[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]
    print(numOfSpanningTree(graph, V))
