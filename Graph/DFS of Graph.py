class Solution:
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        visit = set()
        res = []
        def dfs(visit, root):
            if root not in visit:
                visit.add(root)
                nonlocal res
                res.append(root)
                for nei in adj[root]:
                    if nei not in visit:
                        dfs(visit, nei)
                        
        dfs(visit, 0)
        return res