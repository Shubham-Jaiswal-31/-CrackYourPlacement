class Solution:
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr,n):
        #Your code here
        for i in range(n):
            if arr[i] < 0:
                arr[i] = 0
        
        for i in range(n):
            val = abs(arr[i])
            if 1 <= val <= n:
                if arr[val - 1] > 0:
                    arr[val - 1] *= -1
                elif arr[val - 1] == 0:
                    arr[val - 1] = -1 * (n + 1)
        
        for i in range(1, n + 1):
            if arr[i - 1] >= 0:
                return i
        return n + 1