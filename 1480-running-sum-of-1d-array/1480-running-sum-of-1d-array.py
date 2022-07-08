class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Easy Problem: O(n) time, O(1) space.
        for i in range(1, len(nums)):
            nums[i] = nums[i-1] + nums[i]
            
        return nums