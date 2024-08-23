class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u, v in adjacentPairs:
            adj[u].append(v)
            adj[v].append(u)

        startPoint = -1
        res = []
        for v in adj:
            if len(adj[v]) == 1:
                startPoint = v
                break

        def dfs(u, prev):
            res.append(u)
            for nei in adj[u]:
                if nei != prev:
                    dfs(nei, u)

        dfs(startPoint, float('-inf'))
        return res