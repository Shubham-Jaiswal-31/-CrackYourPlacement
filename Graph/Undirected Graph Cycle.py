from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        visit = [0] * V
        
        def dfs(root, par):
            visit[root] = 1
            for nei in adj[root]:
                if not visit[nei]:
                    if dfs(nei, root):
                        return True
                elif nei != par:
                    return True
            return False
            
        for i in range(V):
            if not visit[i]:
                if dfs(i, -1):
                    return True
        return False
        