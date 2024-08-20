class Solution:
    #Function to find the maximum number of cuts.
    def maximizeTheCuts(self,n,x,y,z):
        dp = [-1] * (n + 1)
        
        def dfs(n):
            
            if n == 0:
                return 0
            if n < 0:
                return float('-inf')
            if dp[n] != -1:
                return dp[n]
                
            a = 1 + dfs(n - x)
            b = 1 + dfs(n - y)
            c = 1 + dfs(n - z)
            dp[n] = max(a, b, c)
            return dp[n]
            
        ans = dfs(n)
        if ans < 0:
            return 0
        else:
            return ans