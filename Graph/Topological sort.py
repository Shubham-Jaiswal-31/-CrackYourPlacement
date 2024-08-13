class Solution:
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        visit = set()
        stack = []
        
        def dfs(node):
            visit.add(node)
            for nei in adj[node]:
                if nei not in visit:
                    dfs(nei)
            stack.append(node)
        
        for i in range(V):
            if i not in visit:
                dfs(i)
        
        res = []
        while stack:
            res.append(stack.pop())
        return res