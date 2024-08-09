from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:

        q = Queue(V)
        q.put(0)
        res = []
        visit = [False] * len(adj)
        visit[0] = True
        
        while not q.empty():
            nxt = q.get()
            res.append(nxt)
            for nei in adj[nxt]:
                if visit[nei] == False:
                    visit[nei] = True
                    q.put(nei)
        return res