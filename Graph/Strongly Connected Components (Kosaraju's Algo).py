class Solution:
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        vis = [0] * V
        stack = []
        
        def dfs(node, adj):
            vis[node] = 1
            for nei in adj[node]:
                if not vis[nei]:
                    dfs(nei, adj)
            stack.append(node)
            
        def dfs3(node, adjT):
            vis[node] = 1
            for nei in adjT[node]:
                if not vis[nei]:
                    dfs3(nei, adjT)
        
        for i in range(V):
            if not vis[i]:
                dfs(i, adj)
            
        adjT = [[] for _ in range(V)]
        for i in range(V):
            vis[i] = 0
            for nei in adj[i]:
                adjT[nei].append(i)
        
        vis = [0] * V
        scc = 0
        while stack:
            node = stack.pop()
            if not vis[node]:
                scc += 1
                dfs3(node, adjT)
        return scc