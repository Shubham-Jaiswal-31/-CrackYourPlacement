from typing import List

class Solution:
    def backtrack(self, i, j, a, n, res, move, vis, di, dj):
        if i == n - 1 and j == n - 1:
            res.append(move)
            return
        
        direction = 'DLRU'
        for ind in range(4):
            nexti = i + di[ind]
            nextj = j + dj[ind]
            if (nexti >= 0 and nextj >= 0 and nexti < n and nextj < n 
               and not vis[nexti][nextj] and a[nexti][nextj] == 1):
                vis[i][j] = 1
                self.backtrack(nexti, nextj, a, n, res, move + direction[ind], vis, di, dj)
                vis[i][j] = 0
            
    def findPath(self, m: List[List[int]]) -> List[str]:
        res = []
        vis = [[0] * n for _ in range(n)]
        di = [1, 0, 0, -1]
        dj = [0, -1, 1, 0]
        if m[0][0] == 1:
            self.backtrack(0, 0, m, len(m), res, '', vis, di, dj)
        return res