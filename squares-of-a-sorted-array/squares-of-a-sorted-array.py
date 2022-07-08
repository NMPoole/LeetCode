class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # First, square all numbers in nums for O(n) time.
        for i, num in enumerate(nums):
            nums[i] = num * num
            
        # Then, sort the nums array in presumably O(n logn) time.
        return sorted(nums)
        