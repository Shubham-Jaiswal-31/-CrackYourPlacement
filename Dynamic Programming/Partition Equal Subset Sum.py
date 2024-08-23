class Solution:
    def equalPartition(self, N, nums):
        if sum(nums) % 2:
            return False
        
        dp = set([0])
        target = sum(nums) // 2
        for i in range(N - 1, -1, -1):
            nextDP = dp.copy()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                nextDP.add(t + nums[i])
            dp = nextDP
        return False