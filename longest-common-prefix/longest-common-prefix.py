class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Solution: O(n) time, O(1) additional space.
        # Longest common prefix will be the intersection between the minimum and maximum string.
        
        if not strs or len(strs) == 0:
            return ""
        
        max_str, min_str = max(strs), min(strs)
        match = 0
        
        while match < len(max_str) and match < len(min_str) and max_str[match] == min_str[match]:
            match += 1
            
        return max_str[0:match]