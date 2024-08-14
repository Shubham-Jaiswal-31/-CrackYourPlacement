class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ds = DisjointSet(n * n)
        direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        # connect 1's
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    continue
                for dr, dc in direct:
                    nr, nc = r + dr, c + dc
                    if self.isValid(nr, nc, n) and grid[nr][nc] == 1:
                        ds.unionBySize(r * n + c, nr * n + nc)
        
        # convert each 0 and check
        mx = 0
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    continue
                components = set()
                for dr, dc in direct:
                    nr, nc = r + dr, c + dc
                    if self.isValid(nr, nc, n) and grid[nr][nc] == 1:
                        components.add(ds.findUPar(nr * n + nc))
                sizeTotal = 0
                for c in components:
                    sizeTotal += ds.size[c]
                mx = max(mx, sizeTotal + 1)

        for cell in range(n * n):
            mx = max(mx, ds.size[ds.findUPar(cell)])
        return mx
    
    def isValid(self, r, c, n):
        return r >= 0 and c >= 0 and r < n and c < n
        # connect 1's

class DisjointSet:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)
    
    def findUPar(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]
    
    def unionBySize(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        if ulp_u == ulp_v:
            return
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]