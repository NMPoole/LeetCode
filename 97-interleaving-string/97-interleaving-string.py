class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        # Solution: O(len1 * len2) time, O(len1 * len2) space - space complexity can be made O(len2)!
        len3 = len(s3)
        len1, len2 = len(s1), len(s2)
        
        # Guard: Any interleaving uses all characters.
        if len1 + len2 != len3:
            return False
        
        # Dynamic programming 2D array: (len1+1)*(len2+1) size, plus ones account for empty strings.
        dp = [[False] * (len2 + 1) for i in range(len1 + 1)]
        
        dp[len1][len2] = True
        
        # Start at bottom right of the 2D array, working left first, then up.
        for i in range(len1, -1, -1): # From len1 index (inclusive accounts for plus 1) to 0 index.
            for j in range(len2, -1, -1):
        
                # If i in s1 bounds, check if char at i equal to target char.
                if i < len1 and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                
                # Also, if j in s2 bounds, check if char at j equal to target char.
                if j < len2 and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
                    
                # If neither true, then dp[i][j] is False, which is initialised as such.
                
        return dp[0][0]
        
                
        
