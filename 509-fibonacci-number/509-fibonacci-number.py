class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Iterative Approach: O(n) time, O(1) space.
        if n <= 1: return n # Guard condition.
        
        prev1, prev2 = 1, 0
        output = 0
        
        for i in range(2, n + 1):
            output = prev1 + prev2
            
            prev2 = prev1
            prev1 = output
        
        return output
            