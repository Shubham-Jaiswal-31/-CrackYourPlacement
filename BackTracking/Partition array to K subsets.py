class Solution:
    def isKPartitionPossible(self, a, k):
        n = len(a)
        total_sum = sum(a)
        target_sum = total_sum // k
        if total_sum % k != 0:
            return False

        self.memo = {}

        def dfs(subset_sum, k):
            if k == 0:
                return True
            if subset_sum == target_sum:
                return dfs(0, k-1)

            key = tuple(used)
            if key in self.memo:
                return self.memo[key]

            for i in range(n):
                if used[i]:
                    continue
                if subset_sum + a[i] > target_sum:
                    break
                used[i] = True
                if dfs(subset_sum+a[i], k):
                    key = tuple(used)
                    self.memo[key] = True
                    return True
                used[i]= False

            key = tuple(used)
            self.memo[key] = False

        used = [False for _ in range(n)]
        a.sort(reverse=True)
        return dfs(0, k)