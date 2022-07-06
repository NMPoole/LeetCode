class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_str = str(abs(x))
        x_str.rstrip("0") # Remove any zeros from the end of the string.
        x_str = x_str[::-1] # Reverse the string.
        x_rev = int(x_str) # Convert back to integer (breaks assumption!)
        
        if x_rev >= (2**31 - 1) or x_rev <= -2**31: # Out of bounds.
            return 0
        elif x < 0: # Number was negative.
            return -x_rev
        else:
            return x_rev
        