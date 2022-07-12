class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Solution: 
        #   For every number (1 to n) seen, negate the value at the number's index.
        #   E.g., if first num is 4, mark the 4th number (index is 3) as its negation.
        #   Then, all positive nums left in nums represent indices whose numbers were unseen.
        #   O(n) time, O(1) additional space.
        output = []
        
        for num in nums:
            nums[abs(num) - 1] = -abs(nums[abs(num) - 1])
            
        for i in range(len(nums)):
            if nums[i] > 0:
                output.append(i + 1)
                
        return output