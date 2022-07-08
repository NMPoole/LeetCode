class Solution(object):
    def minCost(self, houses, cost, m, n, target):
        """
        :type houses: List[int]
        :type cost: List[List[int]]
        :type m: int
        :type n: int
        :type target: int
        :rtype: int
        """
        # Maps (i, t, p) -> the minimum cost to paint houses i <= h < m with t neighborhoods, where house i-1 is color p.
        dp = {}
        
        # Define recursive function.
        def dfs(i, t, p):
            key = (i, t, p)
            
            # Base case - trying to color 0 houses. Only i == len(houses) is necessary to check here, but it prunes 
            # some of the search space to make things faster.
            if i == len(houses) or t < 0 or m - i < t:
                if t == 0 and i == len(houses): return 0
                else: return float('inf')
            
            # Recursive step.
            if key not in dp:
                if houses[i] == 0:
                    dp[key] = min(dfs(i + 1, t - (nc != p), nc) + cost[i][nc - 1] for nc in range(1, n + 1))
                else:
                    dp[key] = dfs(i + 1, t - (houses[i] != p), houses[i])
                
            return dp[key]
            
        ret = dfs(0, target, -1)
        
        # If ret is infinity, then every case failed because there were too many neighborhoods to start.
        # If we could paint over houses that were previously painted, we could remedy that, but not allowed. So, return -1.
        return ret if ret < float('inf') else -1