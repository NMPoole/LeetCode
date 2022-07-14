class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution: O(n) time, O(1) additional space.
        #   XOR of duplicate numbers zero-out, so result after XORing all nums is the one with no duplicate.
        result = nums[0]
        for i in range(1, len(nums)):
            result ^= nums[i]
        return result