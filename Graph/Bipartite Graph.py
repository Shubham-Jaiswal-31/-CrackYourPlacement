from collections import deque
class Solution:
    def isBipartite(self, V, adj):
        odd = [0] * V

        def bfs(i):
            if odd[i]:
                return True
            q = deque([i])
            odd[i] = -1
            while q:
                i = q.popleft()
                for nei in adj[i]:
                    if odd[i] == odd[nei]:
                        return False
                    elif not odd[nei]:
                        q.append(nei)
                        odd[nei] = -1 * odd[i]
            return True
        
        for i in range(V):
            if not bfs(i):
                return False
        return True