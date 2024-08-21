class Solution:
    def getCount(self, n):
        dp = [[-1] * (n + 1) for _ in range(10)]
        mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [-1, 0, -1]]

        def dfs(i, j, n):
            if n == 1:
                return 1
            if dp[mat[i][j]][n] != -1:
                return dp[mat[i][j]][n]
                
            a = dfs(i, j, n - 1)
            b, c, d, e, f = 0, 0, 0, 0, 0
            if j - 1 >= 0 and mat[i][j-1] != -1:
                b = dfs(i, j - 1, n - 1)
            if j + 1 < 3 and mat[i][j+1] != -1:
                c = dfs(i, j + 1, n - 1)
            if i - 1 >= 0 and mat[i-1][j] != -1:
                d = dfs(i - 1, j, n - 1)
            if i + 1 < 4 and mat[i+1][j] != -1:
                e = dfs(i + 1, j, n - 1)
            dp[mat[i][j]][n] = a + b + c + d + e
            return dp[mat[i][j]][n]
        
        ans = 0
        for i in range(4):
            for j in range(3):
                if mat[i][j] != -1:
                    ans += dfs(i, j, n)
        return ans