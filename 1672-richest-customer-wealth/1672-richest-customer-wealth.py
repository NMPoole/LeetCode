class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        # Pythonic Solution: O(n * m) time, O(1) space.
        #   Map applies sum() to each item in accounts. 
        #   Each item is a list representing the wealth of a customer.
        #   max() gets the max value of all the items returned by map().
        return max(map(sum, accounts))