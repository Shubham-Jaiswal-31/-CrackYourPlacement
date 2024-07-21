class Solution:
    def solveWordWrap(self, nums, k):
        #Code here
        self.n = len(nums)
        dp = [-1] * self.n
        return self.solve(nums, k, 0, dp)

    def solve(self, nums, k, idx, dp):
        if idx >= self.n:
            return 0
        if dp[idx] != -1:
            return dp[idx]
        
        ans = float('inf')
        sum = 0
        for i in range(idx, self.n):
            sum += nums[i]
            if k >= sum and i == self.n - 1:
                ans = min(ans, self.solve(nums, k, i + 1, dp))
            elif k >= sum:
                x = k - sum
                x = x * x
                ans = min(ans, x + self.solve(nums, k, i + 1, dp))
            sum += 1 

        dp[idx] = ans
        return ans
