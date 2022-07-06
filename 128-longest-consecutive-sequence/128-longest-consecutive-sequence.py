class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution in O(n) time, with O(n) memory.
        
        nums = set(nums) # Remove duplicates as not consecutive.
        output = 0
        
        for n in nums:
            
            if n - 1 not in nums: # Potential beginning of sequence.
                
                # Find sequence of consecutive nums.
                start = n
                while start in nums:
                    start += 1
                    
                # Max of largest seq so far, and curr seq.
                output = max(output, start - n)
        
        return output