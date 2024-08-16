from typing import List
class Solution:
    def minCashFlow(self, transaction: List[List[int]], n: int) -> List[List[int]]:
        frds = [0] * n
        for i in range(n):
            for j in range(n):
                frds[i] += transaction[j][i] - transaction[i][j]
        
        ans = [[0] * n for _ in range(n)]
        
        while True:
            minIndex = frds.index(min(frds))
            maxIndex = frds.index(max(frds))
            
            if frds[minIndex] == 0 and frds[maxIndex] == 0:
                break
            
            mini = min(-frds[minIndex], frds[maxIndex])
            
            ans[minIndex][maxIndex] += mini
            frds[minIndex] += mini
            frds[maxIndex] -= mini
        return ans