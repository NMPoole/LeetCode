class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Solution has O(n) time complexity, and O(n) space complexity.
        values = {} # Dictionary of values in nums to their corresponding index.
        
        for i, val in enumerate(nums):
            if target - val in values: # If the number required in dictionary, we have the answer.
                return [values[target - val], i]
            else: # Otherwise, make an entry for the current value.
                values[val] = i