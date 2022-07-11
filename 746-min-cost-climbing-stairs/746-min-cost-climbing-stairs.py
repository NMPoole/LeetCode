class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        
        # Min cost for first 2 positions simply their values.
        prev2 = cost[0]
        prev1 = cost[1]
        
        # Min cost for all other positions is value at pos plus 
        #   the minimum of the costs that we could step from.
        for i in range(2, n):
            temp = cost[i] + min(prev1, prev2)
            prev2 = prev1
            prev1 = temp
            
        # Can reach top by stepping from penultimate or last step, so consider both.
        return min(prev2, prev1)