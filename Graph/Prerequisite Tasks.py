from collections import deque
class Solution:
    def isPossible(self,V,P,prerequisites):
        adj = [[] for _ in range(V)]
        for u, v in prerequisites:
            adj[u].append(v)
        
        indegree = [0] * V
        for i in range(V):
            for nei in adj[i]:
                indegree[nei] += 1
        
        q = deque()
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
        
        topo = []
        while q:
            node = q.popleft()
            topo.append(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
            
        if len(topo) == V:
            return True
        return False