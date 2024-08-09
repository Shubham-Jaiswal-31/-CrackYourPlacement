from typing import List

class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        vis = [0] * V
        pathVis = [0] * V
        
        def dfs(node):
            vis[node] = 1
            pathVis[node] = 1
            
            for cur in adj[node]:
                if not vis[cur]:
                    if dfs(cur):
                        return True
                elif pathVis[cur]:
                    return True
                    
            pathVis[node] = 0
            return False
        
        for i in range(V):
            if not vis[i]:
                if dfs(i):
                    return True
        return False