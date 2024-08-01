class Solution:
    def findPair(self, n : int, x : int, arr : List[int]) -> int:
        # code here
        arr.sort()
        
        l, r = 0, 1
        
        while l < n and r < n:
            if arr[r] - arr[l] == x and l != r:
                return 1
            elif arr[r] - arr[l] < x:
                r += 1
            else:
                l += 1
                
        return -1
