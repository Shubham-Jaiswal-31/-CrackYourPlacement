class Solution:
    def studentCount(self, arr, pages):
        stu = 1
        pageStu = 0
        
        for i in range(len(arr)):
            if pageStu + arr[i] <= pages:
                pageStu += arr[i]
            else:
                stu += 1
                pageStu = arr[i]
        return stu
        
    #Function to find minimum number of pages.
    def findPages(self,n ,arr ,m):
        #code here
        if m > n:
            return -1
            
        l, r = max(arr), sum(arr)
        while l <= r:
            mid = (l + r) // 2
            noStu = self.studentCount(arr, mid)
            if noStu > m:
                l = mid + 1
            else:
                r = mid - 1
                
        return l
