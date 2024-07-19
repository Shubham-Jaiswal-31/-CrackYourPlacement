class Solution:
    def uniquePerms(self, arr, n):
        res=[]
        visited=[False]*n
        curr=[]
        s=set()
        arr.sort()
        self.dfs(arr,visited,s,curr,res)
        return res
        
    def dfs(self, arr, visited, s, curr, res):
        n=len(arr)
        if len(curr)==n:
            curr_tuple=tuple(curr)
            if curr_tuple not in s:
                s.add(curr_tuple)
                res.append(curr.copy())
            return
        for i in range(n):
            if visited[i]==False:
                visited[i]=True
                curr.append(arr[i])
                self.dfs(arr,visited,s,curr,res)
                visited[i]=False
                curr.pop()
