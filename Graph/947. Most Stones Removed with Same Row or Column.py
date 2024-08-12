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

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        R, C = 0, 0
        for r, c in stones:
            R = max(R, r)
            C = max(C, c)
        ds = DisjointSet(R + C + 1)
        stoneNodes = {}
        for r, c in stones:
            c += R + 1
            ds.unionBySize(r, c)
            stoneNodes[r] = 1
            stoneNodes[c] = 1
        
        count = 0
        for v in stoneNodes:
            if ds.findUPar(v) == v:
                count += 1
        return len(stones) - count
