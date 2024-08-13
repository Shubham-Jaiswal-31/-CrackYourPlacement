class Solution:
    def isNegativeWeightCycle(self, n, edges):
        visited = [0] * n
        dist = [0] * n
        
        def isNegCycleBellmanFord(src, dist):
            for i in range(n):
                dist[i] = 10**18
            dist[src] = 0
        
            for i in range(1, n):
                for j in range(m):
                    u = edges[j][0]
                    v = edges[j][1]
                    weight = edges[j][2]
                    if (dist[u] != 10**18 and dist[u] + weight < dist[v]):
                        dist[v] = dist[u] + weight
        
            for i in range(m):
                u = edges[i][0]
                v = edges[i][1]
                weight = edges[i][2]
                if (dist[u] != 10**18 and dist[u] + weight < dist[v]):
                    return True
         
            return False
        
        for i in range(n):
            if (visited[i] == 0):
                if (isNegCycleBellmanFord(i, dist)):
                    return 1
                for i in range(n):
                    if (dist[i] != 10**18):
                        visited[i] = True
        return 0