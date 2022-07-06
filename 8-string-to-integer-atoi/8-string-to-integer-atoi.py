class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip() # Whitespace trimmed string.
        if s is None or len(s) < 1: # Base Condition.
            return 0
        
        i = 0
        isNeg = s[0] == '-'
        
        if s[0] == '-' or s[0] == '+': # Skip over sign if present.
            i += 1
            
        number = 0 # This will store the converted number
        
        # Loop for each numeric character in the string iff 
        # numeric characters are leading characters in the string.
        while i < len(s) and '0' <= s[i] <= '9':
            number = number * 10 + (ord(s[i]) - ord('0'))
            i += 1
            
        # Give back the sign to the number.
        if isNeg:
            number = -number
            
        # Max and Min values for the integers.
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
            
        # Edge cases - integer overflow and underflow.
        if number < INT_MIN:
            return INT_MIN
        if number > INT_MAX:
            return INT_MAX
        
        return number