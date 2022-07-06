class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = defaultdict(int)
        
        for char in s:
            counts[char] += 1
        
        for i, char in enumerate(s):
            if counts[char] == 1:
                return i
        
        return -1
        