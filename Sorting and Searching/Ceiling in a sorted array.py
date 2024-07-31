class Solution:
    def findCeil(self,A,N,X):
        #Your code here
        l = 0
        h = len(A)-1
        mid = 0
        ind = -1
        while(l<=h):
            mid = (l+h)//2
            if A[mid]==X:
                return A[mid]
            elif A[mid]<=X:
                l = mid+1
            else:
                ind = A[mid]
                h = mid-1
        return ind


    def findFloor(self,A,N,X):
        #Your code here
        l = 0
        h = len(A)-1
        mid = 0
        ind = -1
        while(l<=h):
            mid = (l+h)//2
            if A[mid]==X:
                return mid
            elif A[mid]<=X:
                ind = mid
                l = mid+1
            else:
                h = mid-1
        return ind
