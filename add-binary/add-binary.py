class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # Solution: O(n) time, O(1) additional space.
        
        output = ""
        carry = 0
        
        a, b = a[::-1], b[::-1]
        
        for i in range(max(len(a), len(b))):
            
            digitA = ord(a[i]) - ord("0") if i < len(a) else 0
            digitB = ord(b[i]) - ord("0") if i < len(b) else 0
            
            total = digitA + digitB + carry
            output = str(total % 2) + output
            carry = total // 2
            
        if carry:
            output = "1" + output
            
        return output