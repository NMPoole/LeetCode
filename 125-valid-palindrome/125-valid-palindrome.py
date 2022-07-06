class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s) - 1
        
        while l < r:
            
            # Skip over non-alphanumeric chars.
            while l < r and not self.isAlphaNum(s[l]):
                l += 1
            while r > l and not self.isAlphaNum(s[r]):
                r -= 1
            
            # Check chars are the same on both sides.
            if s[l].lower() != s[r].lower():
                return False
            
            l, r = l + 1, r - 1
            
        return True
            

    def isAlphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))
        