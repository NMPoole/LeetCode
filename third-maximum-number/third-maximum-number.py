class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Keep track of largest, 2nd largest, and 3rd largest numbers in a list, respectively.
        v = [float('-inf'), float('-inf'), float('-inf')]
        
        for num in nums:
            
            if num not in v: # Update maximums based on current unseen number.
                if num > v[0]:   v = [num, v[0], v[1]]
                elif num > v[1]: v = [v[0], num, v[1]]
                elif num > v[2]: v = [v[0], v[1], num]
                    
        # If there is not a 3rd max, return the maximum overall, else return v[2] (i.e., 3rd largest).
        return max(nums) if float('-inf') in v else v[2]