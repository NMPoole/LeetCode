class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        seen = defaultdict(lambda:-1) # Dictionary of seen numbers to corresponding index.
        
        # Linear search over elements, adding nums to seen, checking for double element existence.
        for i, num in enumerate(arr):
            
            # Check both if number twice as big or twice as small already seen.
            # By default, the two indices are different (i.e., i != j)
            if seen[num * 2] != -1:
                return True
            if num % 2 == 0 and seen[num / 2] != -1:
                return True
            
            seen[num] = i
            
        return False