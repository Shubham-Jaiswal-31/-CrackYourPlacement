class Solution:
    #Function to find maximum of minimums of every window size.
    def maxOfMin(self,arr,n):
        s = [] # stack
        left = [-1] * (n + 1)
        right =  [n] * (n + 1)
        
        for i in range(n):
            while s and arr[s[-1]] >= arr[i]:
                s.pop()
            
            if s:
                left[i] = s[-1]
            s.append(i)
        
        s = []
        for i in range(n - 1, -1, -1):
            while s and arr[s[-1]] >= arr[i]:
                s.pop()
            
            if s:
                right[i] = s[-1]
            s.append(i)
            
        ans = [0] * (n + 1)
        for i in range(n):
            length = right[i] - left[i] - 1
            ans[length] = max(ans[length], arr[i])
            
        for i in range(n - 1, -1, -1):
            ans[i] = max(ans[i], ans[i + 1])
        
        return ans[1:]