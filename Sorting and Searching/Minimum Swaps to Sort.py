class Solution:
  #Function to find the minimum number of swaps required to sort the array.
  def minSwaps(self, nums):
    #Code here
    pair = [[nums[i], i] for i in range(len(nums))]
    pair.sort()
    
    res = 0
    i = 0
    while i < len(nums):
      j = pair[i][1] 
      if j == i:
        i += 1
        continue
        
      pair[i], pair[j] = pair[j], pair[i]
      res += 1
          
    return res