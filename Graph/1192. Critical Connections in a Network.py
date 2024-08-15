class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.timer = 1
        adj = [[] for _ in range(n)]
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)
        vis = [0] * n
        tin = [0] * n
        low = [0] * n
        res = []

        def dfs(node, parent):
            vis[node] = 1
            tin[node] = low[node] = self.timer
            self.timer += 1
            for nei in adj[node]:
                if nei == parent: 
                    continue
                if vis[nei]:
                    low[node] = min(low[node], low[nei])
                else:
                    dfs(nei, node)
                    low[node] = min(low[node], low[nei])
                    if low[nei] > tin[node]:
                        res.append([nei, node])
        dfs(0, -1)
        return res