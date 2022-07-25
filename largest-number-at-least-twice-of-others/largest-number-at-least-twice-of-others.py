class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution: O(n) time, O(1) additional space.
        
        max_val = max(nums)
        max_idx = nums.index(max_val)
        
        for num in nums:
            if num != max_val and num * 2 > max_val:
                return -1
            
        return max_idx