class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution: O(n) time, and O(1) additional space.
        
        S = sum(nums)
        left_sum = 0
        
        for i, x in enumerate(nums):
            
            if left_sum == (S - left_sum - x): # Check if left- and right-ward sums are the same.
                return i
            
            left_sum += x # Otherwise, simply increase the left-ward sum.
            
        return -1 # No pivot index found.
        