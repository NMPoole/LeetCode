class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # Solution: O(n) time, O(1) space.
        
        n = len(arr)
        maxVal = arr[n-1] # Max value seen to the right of current index so far.
        arr[n-1] = -1 # Last index always becomes -1 as nothing to the right.
        
        # Update all nums to max value seen to right so far.
        for i in range(n-2, -1, -1):
            temp = arr[i]
            arr[i] = maxVal
            maxVal = max(maxVal, temp)
            
        return arr
        