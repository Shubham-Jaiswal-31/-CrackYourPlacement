class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        zero, sx, sy = 0, 0, 0
        R, C = len(grid), len(grid[0])
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    zero += 1
                elif grid[r][c] == 1:
                    sx, sy = r, c

        def dfs(x, y, zero):
            if x < 0 or y < 0 or x >= R or y >= C or grid[x][y] == -1:
                return 0
            if grid[x][y] == 2:
                return 1 if zero == -1 else 0
            grid[x][y] = -1
            zero -= 1
            paths = dfs(x + 1, y, zero) + dfs(x, y + 1, zero) + \
                    dfs(x - 1, y, zero) + dfs(x, y - 1, zero)
            grid[x][y] = 0
            zero += 1
            return paths
        return dfs(sx, sy, zero)