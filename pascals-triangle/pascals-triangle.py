class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # Solution: O(numRows ^ 2) time, O(1) additional space.
        
        output = [[1]] # First row of Pascal's triangle.
        
        # Every row begins and ends with 1. All elements between are sum of above two elements.
        for r in range(2, numRows + 1):
            
            tmp = [1]
            for c in range(1, r - 1):
                tmp.append(output[-1][c] + output[-1][c - 1])
            tmp.append(1)
            
            output.append(tmp)
            
        return output