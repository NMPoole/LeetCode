class Solution(object):
    
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution: O(n) time, O(1) additional space.
        
        if len(nums) < 2:
            return len(nums)
        
        i = 0  # Slow-run pointer.
        for j, value in enumerate(nums):
            if value == nums[i]:
                continue
            # Else, capture the result
            i += 1
            if i != j:
                nums[i] = value # In place overriden.
 
        return i + 1
            
        