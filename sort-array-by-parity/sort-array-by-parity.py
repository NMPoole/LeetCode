class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Solution: Use quicksort to do the sort in place - O(n) time, O(1) additional space.
        i, j = 0, len(nums) - 1
        
        while i < j:
            
            if nums[i] % 2 > nums[j] % 2:
                nums[i], nums[j] = nums[j], nums[i]

            if nums[i] % 2 == 0: i += 1
            if nums[j] % 2 == 1: j -= 1

        return nums