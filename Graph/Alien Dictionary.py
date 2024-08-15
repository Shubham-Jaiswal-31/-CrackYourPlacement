class Solution:
    def findOrder(self,alien_dict, N, K):
        adj = {c:set() for w in alien_dict for c in w}
        
        for i in range(N - 1):
            w1, w2 = alien_dict[i], alien_dict[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ''
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        visit = {} # False: visited, True: current path
        res = []
        
        def dfs(c):
            if c in visit:
                return visit[c]
            visit[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visit[c] = False
            res.append(c)
                
        for c in adj:
            if dfs(c):
                return ''
        res.reverse()    
        return ''.join(res)
