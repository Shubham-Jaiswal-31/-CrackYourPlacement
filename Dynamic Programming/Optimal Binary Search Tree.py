class Solution:
    def optimalSearchTree(self, keys, freq, n):
        dp = [["."]*n for i in range(n)]
        
        for g in range(n):
            for i,j in zip(range(n-g),range(g,n)):  
                if g==0:
                    dp[i][j]=freq[i]
                        
                elif g==1:
                    f1 = freq[i]
                    f2 = freq[j]
                    dp[i][j]=min(f1+2*f2,2*f1+f2)
                        
                else:
                    Min = 10e9+7
                    freqSum = 0
                    for x in range(i,j+1):
                        freqSum+=freq[x]
                        
                    for k in range(i,j+1):
                        if k==i:
                            left=0
                        else:    
                            left = dp[i][k-1] 
                        if k==j:
                            right = 0
                        else:
                            right = dp[k+1][j]
                        if left+right+freqSum<Min:
                            Min = left+right+freqSum
                    dp[i][j]=Min    
        
        return dp[0][n-1]     
