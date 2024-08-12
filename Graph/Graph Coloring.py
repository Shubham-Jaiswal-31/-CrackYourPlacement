# M-Coloring Problem
#Function to determine if graph can be coloured with at most M colours such
#that no two adjacent vertices of graph are coloured with same colour.
def graphColoring(graph, k, V):
    color = [0] * V
    
    def safe(node, col):
        for i in range(V):
            if i != node and graph[i][node] == 1 and color[i] == col:
                return False
        return True
    
    def dfs(node):
        if node == V:
            return True
        
        for i in range(1, k + 1):
            if safe(node, i):
                color[node] = i
                if dfs(node + 1):
                    return True
                color[node] = 0
        return False
                
    return dfs(0)