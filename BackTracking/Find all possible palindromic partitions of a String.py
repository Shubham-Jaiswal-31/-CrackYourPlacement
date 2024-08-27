class Solution:
    def allPalindromicPerms(self, S):
        res = []
        part = []

        def dfs(i):
            if i == len(S):
                res.append(part.copy())
                return
            for j in range(i, len(S)):
                if self.isPal(S, i, j):
                    part.append(S[i:j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return res
    
    def isPal(self, S, l, r):
        while l < r:
            if S[l] != S[r]:
                return False
            l += 1
            r -= 1
        return True