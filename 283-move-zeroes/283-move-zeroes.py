class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if (n == 0 or n == 1): return
        
        l = 0; # Left pointer, which points to first zero left or right pointer.
        
        for r in range(n): # Right pointer loops over all elements.
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                
        