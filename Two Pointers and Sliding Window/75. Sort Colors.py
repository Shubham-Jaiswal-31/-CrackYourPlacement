class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = m = 0
        r = len(nums) - 1
        while m <= r:
            if not nums[m]:
                nums[l], nums[m] = nums[m], nums[l]
                m += 1
                l += 1 
            elif nums[m] == 1:
                m += 1
            else:
                nums[r], nums[m] = nums[m], nums[r]
                r -= 1 
        