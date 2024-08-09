from collections import deque
class Solution:
    #Function to find out minimum steps Knight needs to reach target position.
    def minStepToReachTarget(self, KnightPos, TargetPos, N):    
        def isValid(i, j, n):
            if i >= 0 and i < n and j >= 0 and j < n and not visit[i][j]:
                return True
            return False
        
        tx, ty = TargetPos[0] - 1, TargetPos[1] - 1
        x1, y1 = KnightPos[0] - 1, KnightPos[1] - 1
        
        if x1 == tx and y1 == ty:
            return 0
        
        visit = [[False] * N for _ in range(N)]
        q = deque([[x1, y1]])
        visit[x1][y1] = True
        
        res = 0
        while q:
            res += 1
            for _ in range(len(q)):
                x, y = q.popleft()
                pos = [[1, 2], [1, -2], [-1, 2], [-1, -2],
                       [2, 1], [-2, 1], [2, -1], [-2, -1]]
                for i in range(8):
                    nx = x + pos[i][0]
                    ny = y + pos[i][1]
                    
                    if nx == tx and ny == ty:
                        return res
                        
                    if isValid(nx, ny, N):
                        visit[nx][ny] = True
                        q.append([nx, ny])
                
        return res