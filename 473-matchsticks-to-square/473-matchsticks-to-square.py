class Solution(object):
    def makesquare(self, matchsticks):
        """
        :type matchsticks: List[int]
        :rtype: bool
        """
        n = len(matchsticks)
        perimeter = sum(matchsticks)
        
        if perimeter % 4 != 0: # Guard Condition: Can't have 4 equal sides if not divisible by 4.
            return False
        else:
            side = perimeter // 4 # Expected length of side if sum of matchsticks is divisible by 4.
            
        matchsticks.sort(reverse=True) # Sort in descending order to better avoid non-optimal searches in recursive tree.
        
        def dfs(a, b, c, d, i):
            """
            type a: int
            type b: int
            type c: int
            type d: int
            :rtype: bool
            """
            # Solution: O(4^n) time!
            # Base Case: After having assigned all matchsticks to a side, check if obtained a square.
            if i == n: 
                return a == b == c == d
            
            # Recursive Step: Assign current matchstick, m, to all sides recursively.
            m = matchsticks[i]
            
            if a + m <= side and dfs(a + m, b, c, d, i + 1):
                return True
            if b + m <= side and dfs(a, b + m, c, d, i + 1):
                return True
            if c + m <= side and dfs(a, b, c + m, d, i + 1):
                return True
            if d + m <= side and dfs(a, b, c, d + m, i + 1):
                return True
            
            return False
        
        # Start allocating each matchstick to all sides recursively to obtain a valid configuration.
        return dfs(0, 0, 0, 0, 0)