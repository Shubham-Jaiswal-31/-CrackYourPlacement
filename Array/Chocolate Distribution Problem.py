class Solution:
    def findMinDiff(self, A,N,M):
        A.sort()
        res = float('inf')
        i = 0
        while i + M - 1 < N:
            res = min(res, A[i + M - 1] - A[i])
            i += 1
        
        return res
