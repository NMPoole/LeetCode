class Solution(object):
    
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        # Solution: O(n m) time - n is num words and m is length of words - O(n) additional space.
        
        output = []
        
        for word in words:
            if self.check(word, pattern):
                output.append(word)
                
        return output
    
    
    def check(self, word, pattern):
        m1, m2 = {}, {}

        for a, b in zip(word, pattern): # Check over characters to verify bijection.
            if a not in m1: 
                m1[a] = b
            if b not in m2: 
                m2[b] = a

            if a != m2[b] or b != m1[a]:
                return False

        return True
        
        