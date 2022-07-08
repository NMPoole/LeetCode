class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        i, n = 0, len(arr)
        
        while i < n-1:
            if arr[i] == 0: # Need to duplicate the zero.
                
                if i + 2 < n: arr[i+2:n] = arr[i+1:n-1] # Shift array via slicing.
                arr[i+1] = 0 # Add the duplicate zero.
                i += 1 # Progress the counter an additional place to skip over added zero.
                
            i += 1 # Proceed to next
