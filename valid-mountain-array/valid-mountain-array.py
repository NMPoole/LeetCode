class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        fwd, bwd, n = 0, len(arr) - 1, len(arr) # Forwards pointer, backwards pointer, array length.
        
        # Loop forward pointer as long as strictly increasing.
        while fwd + 1 < n and arr[fwd] < arr[fwd + 1]:
            fwd += 1
            
        # Loop backward pointer as long as strictly descreasing.
        while bwd > 0 and arr[bwd - 1] > arr[bwd]: 
            bwd -= 1
            
        # Mountain array if forward and backward pointer equal and within array range.
        return 0 < fwd == bwd < n - 1