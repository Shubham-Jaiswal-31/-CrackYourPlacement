import sys
sys.setrecursionlimit(10**8)
class Solution:
    def __init__(self):
        self.ROW = 0
        self.COL = 0
        self.grid = []
        
    def DFS(self, i, j):
        if (i < 0 or i >= self.ROW or
            j < 0 or j >= self.COL or
            self.grid[i][j] != 1):
            return

        self.grid[i][j] = -1

        self.DFS(i - 1, j - 1)
        self.DFS(i - 1, j)
        self.DFS(i - 1, j + 1)
        self.DFS(i, j - 1)
        self.DFS(i, j + 1)
        self.DFS(i + 1, j - 1)
        self.DFS(i + 1, j)
        self.DFS(i + 1, j + 1)
        
    def numIslands(self,grid):
        #code here
        self.ROW = len(grid)
        self.COL = len(grid[0])
        self.grid = grid
        
        count = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                if self.grid[i][j] == 1:
                    self.DFS(i, j)
                    count += 1
        
        return count
