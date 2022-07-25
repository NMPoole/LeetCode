class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Solution: 
        #   O(logn) time, and O(1) additional space.
        #   Left- and right-ward binary search on target using built-in Pythin functions.
        
        if not nums:
            return [-1, -1]
        
        n = len(nums)
        start, end = -1, -1
        
        # Binary search for left and right insert positons of target to maintain sorted order.
        left = bisect_left(nums, target)
        right = bisect_right(nums, target)
        
        if left < n and nums[left] == target:
            start = left
        if nums[right - 1] == target:
            end = right - 1
            
        return [start, end]