class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        if n <= 1:
            return n
        
        # Two pointer O(n) solution:
        # Ignore equalities, up and down counter ensure subsequent ups/downs only considered once.
        # I.e., the removal of all equalities and subsequent ups/downs is greatest length subsequence.
        up = 1
        down = 1
        
        for i in range(0, n - 1):
            if nums[i] < nums[i + 1]: # Uphill case.
                up = down + 1
            elif nums[i] > nums[i + 1]: # Downhill case.
                down = up + 1
                
        return max(up, down)
                